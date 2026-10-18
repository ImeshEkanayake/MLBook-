"""Execute one self-contained notebook in a fresh kernel using this exact interpreter."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile
import time

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('notebook', nargs='?', default='notebooks/001_Chapter_18_01_Decision_Tree.ipynb')
    parser.add_argument('--output', help='Executed notebook path; defaults to ignored build directory')
    args = parser.parse_args()
    source = (root / args.notebook).resolve()
    destination = (root / args.output).resolve() if args.output else root / 'build' / (source.stem + '.executed.ipynb')
    nb = nbformat.read(source, as_version=4)
    # Stored outputs never substitute for executing a cell in this fresh kernel.
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
    nbformat.validate(nb)
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix='mlbook-kernel-') as temp:
        kernel_dir = Path(temp) / 'python3'
        kernel_dir.mkdir()
        (kernel_dir / 'kernel.json').write_text(json.dumps({
            'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
            'display_name': 'MLBook isolated run', 'language': 'python',
            'env': {'MPLBACKEND': 'module://matplotlib_inline.backend_inline',
                    'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1', 'MKL_NUM_THREADS': '1'}
        }))
        manager = KernelManager(kernel_name='python3',
                                kernel_spec_manager=KernelSpecManager(kernel_dirs=[temp]))
        client = NotebookClient(nb, km=manager, timeout=120, allow_errors=False,
                                resources={'metadata': {'path': str(source.parent)}})
        try:
            client.execute()
        finally:
            if manager.has_kernel:
                manager.shutdown_kernel(now=True)
                manager.cleanup_resources()
    nbformat.validate(nb)
    code_cells = [c for c in nb.cells if c.cell_type == 'code']
    assert all(c.execution_count is not None for c in code_cells)
    assert not any(o.output_type == 'error' for c in code_cells for o in c.outputs)
    destination.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(nb, destination)
    summary = None
    for cell in code_cells:
        for output in cell.outputs:
            if output.output_type == 'stream':
                for line in output.text.splitlines():
                    if line.startswith('EXECUTION_SUMMARY_JSON:'):
                        summary = json.loads(line.split(':', 1)[1])
    if summary is None:
        raise RuntimeError('Notebook must produce its actual execution summary.')
    summary['wall_seconds_including_kernel_start'] = round(time.perf_counter()-started, 3)
    summary['executed_code_cells'] = len(code_cells)
    summary['embedded_png_count'] = sum('image/png' in o.get('data', {}) for c in code_cells for o in c.outputs)
    report = root / 'build' / (summary['example_id'] + '.summary.json')
    report.parent.mkdir(exist_ok=True)
    report.write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))
    print('Executed notebook:', destination)
    print('Machine-readable run summary:', report)


if __name__ == '__main__':
    main()
