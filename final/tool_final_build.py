#!/usr/bin/env python3
"""
Iron Man Mask - final toolbox

Commands:
- preflight: verify required files and Python syntax
- serve-ui: run local HTTP server for configurator_usb.html
- build: create ZIP package with final runtime + tools + docs
"""

from __future__ import annotations

import argparse
import http.server
import json
import os
import py_compile
import socketserver
import sys
import webbrowser
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BUILD_DIR = ROOT / "build"

RUNTIME_FILES = [
    "code.py",
    "config.py",
    "comms.py",
    "logic_core.py",
    "servos.py",
    "laser.py",
    "leds.py",
    "eyes.py",
    "audio_sys.py",
    "ubieranie.py",
]

UI_FILES = [
    "configurator_usb.html",
    "CONFIGURATOR_README.md",
    "assets/jarvis_hud.svg",
]

DOC_FILES = [
    "OPERATIONS_MASTER.md",
]

TOOL_FILES = [
    "tool_final_build.py",
]


def _abs(rel_path: str) -> Path:
    return ROOT / rel_path


def _print(msg: str) -> None:
    sys.stdout.write(msg + "\n")


def check_required_files() -> tuple[list[str], list[str]]:
    required = RUNTIME_FILES + UI_FILES + DOC_FILES + TOOL_FILES
    missing = [p for p in required if not _abs(p).exists()]
    present = [p for p in required if p not in missing]
    return present, missing


def check_python_syntax() -> tuple[list[str], list[tuple[str, str]]]:
    ok: list[str] = []
    errors: list[tuple[str, str]] = []
    py_files = sorted([p for p in ROOT.glob("*.py") if p.is_file()])
    for f in py_files:
        try:
            py_compile.compile(str(f), doraise=True)
            ok.append(f.name)
        except py_compile.PyCompileError as e:
            errors.append((f.name, str(e)))
    return ok, errors


def cmd_preflight(_: argparse.Namespace) -> int:
    _print("== PREFLIGHT ==")

    present, missing = check_required_files()
    _print(f"Required files present: {len(present)}")
    _print(f"Required files missing: {len(missing)}")
    if missing:
        for m in missing:
            _print(f"  MISSING: {m}")

    ok, errors = check_python_syntax()
    _print(f"Python syntax OK: {len(ok)}")
    if errors:
        _print(f"Python syntax errors: {len(errors)}")
        for file_name, err in errors:
            _print(f"  ERROR in {file_name}")
            _print(f"    {err}")

    if missing or errors:
        _print("PREFLIGHT RESULT: FAIL")
        return 1

    _print("PREFLIGHT RESULT: PASS")
    return 0


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def cmd_serve_ui(args: argparse.Namespace) -> int:
    port = int(args.port)
    os.chdir(ROOT)
    url = f"http://127.0.0.1:{port}/configurator_usb.html"

    handler = http.server.SimpleHTTPRequestHandler
    with ReusableTCPServer(("", port), handler) as httpd:
        _print(f"Serving: {ROOT}")
        _print(f"Open URL: {url}")
        _print("Press Ctrl+C to stop.")
        if not args.no_browser:
            try:
                webbrowser.open(url, new=2)
            except Exception:
                _print("Could not auto-open browser. Open URL manually.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            _print("\nStopped.")
    return 0


def list_files_for_package() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part.startswith(".") for part in rel.parts):
            continue
        if rel.parts[0] in {"build", "__pycache__"}:
            continue
        if p.suffix in {".pyc"}:
            continue
        out.append(p)
    return sorted(out)


def cmd_build(args: argparse.Namespace) -> int:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%SZ")
    zip_path = BUILD_DIR / f"maska_final_build_{stamp}.zip"
    manifest_path = BUILD_DIR / f"manifest_{stamp}.json"
    latest_link = BUILD_DIR / "latest_manifest.json"

    files = list_files_for_package()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in files:
            zf.write(file_path, arcname=str(file_path.relative_to(ROOT)))

    manifest = {
        "generated_utc": stamp,
        "workspace": str(ROOT),
        "zip_file": str(zip_path.name),
        "file_count": len(files),
        "files": [str(p.relative_to(ROOT)) for p in files],
        "notes": [
            "This package does not include /sounds content from CIRCUITPY drive.",
            "Copy startup.wav (and optional open.wav/close.wav) to CIRCUITPY/sounds manually.",
        ],
    }
    manifest_text = json.dumps(manifest, indent=2)
    manifest_path.write_text(manifest_text, encoding="utf-8")
    latest_link.write_text(manifest_text, encoding="utf-8")

    _print("== BUILD COMPLETE ==")
    _print(f"ZIP: {zip_path}")
    _print(f"Manifest: {manifest_path}")
    _print(f"Files packed: {len(files)}")

    if args.preflight:
        _print("Running preflight after build...")
        return cmd_preflight(args)
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Iron Man Mask final toolbox")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_preflight = sub.add_parser("preflight", help="Check required files and Python syntax")
    p_preflight.set_defaults(func=cmd_preflight)

    p_serve = sub.add_parser("serve-ui", help="Start local HTTP server for configurator")
    p_serve.add_argument("--port", type=int, default=8000, help="HTTP port (default: 8000)")
    p_serve.add_argument("--no-browser", action="store_true", help="Do not auto-open browser")
    p_serve.set_defaults(func=cmd_serve_ui)

    p_build = sub.add_parser("build", help="Create ZIP package in ./build")
    p_build.add_argument(
        "--preflight",
        action="store_true",
        help="Run preflight checks after build",
    )
    p_build.set_defaults(func=cmd_build)

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
