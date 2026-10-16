#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量抓取: 读 TSV(url\toutput\t[title])，逐行调用 fetch_qsys_doc.py，失败记录到 _batch_failures.log"""
import subprocess, sys, os, time

tsv = sys.argv[1]
fail_log = os.path.join(os.path.dirname(os.path.abspath(tsv)), '_batch_failures.log')
rows = [l for l in open(tsv, encoding='utf-8').read().splitlines() if l.strip() and not l.startswith('#')]
ok = fail = 0
failures = []
for r in rows:
    parts = r.split('\t')
    url, out = parts[0], parts[1]
    title = parts[2] if len(parts) > 2 else None
    cmd = ['python3', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fetch_qsys_doc.py'), url, '-o', out]
    if title:
        cmd += ['--title', title]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if res.returncode == 0 and 'OK ->' in res.stdout:
            ok += 1
        else:
            fail += 1
            msg = res.stderr.strip()[-300:] or res.stdout.strip()[-300:]
            failures.append((url, out, msg))
            print(f"FAIL {os.path.basename(out)}: {msg[:120]}", file=sys.stderr)
    except subprocess.TimeoutExpired:
        fail += 1
        failures.append((url, out, 'timeout'))
        print(f"TIMEOUT {os.path.basename(out)}", file=sys.stderr)
    time.sleep(0.3)

with open(fail_log, 'w', encoding='utf-8') as f:
    for u, o, m in failures:
        f.write(f"{u}\t{o}\t{m}\n")
print(f"\n完成: 成功 {ok} / 失败 {fail} / 总计 {len(rows)}")
if failures:
    print(f"失败明细已写入 {fail_log}")
