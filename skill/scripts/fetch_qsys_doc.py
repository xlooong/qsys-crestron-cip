#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q-SYS help.qsys.com 文档抓取与 Markdown 转换脚本

用法:
  python3 fetch_qsys_doc.py <url_or_htm_path> -o <output.md> [--title "覆盖标题"]

URL 形式:
  https://help.qsys.com/Content/Schematic_Library/gain.htm   (主站 10.4)
  https://help.qsys.com/DeveloperHelp/Content/Code_Examples/HTTPClient.htm  (DeveloperHelp)
  也可直接传 .htm 文件名, 需配合 --base 指定内容根路径

输出结构:
  # 标题
  > 来源: <url>
  描述段落
  ## 分区 (h3)
  ### 子项 (h4)
  - 列表 / 表格 / 代码块 / 引用(Note/Tip)
"""
import argparse, re, sys, urllib.request, os

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
JUNK_CLASSES = ['MCWebHelpFramesetLink', 'MCTextPopupHotSpot']

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return r.read().decode('utf-8', errors='replace')

def clean_text(s):
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def is_junk(el):
    cls = ' '.join(el.get('class') or [])
    return any(j in cls for j in JUNK_CLASSES)

def table_to_md(table):
    rows = []
    for tr in table.find_all('tr'):
        cells = []
        for td in tr.find_all(['td', 'th']):
            t = clean_text(td.get_text(' ', strip=True))
            t = t.replace('|', '\\|').replace('\n', ' ')
            cells.append(t)
        rows.append(cells)
    if not rows:
        return ''
    ncol = max(len(r) for r in rows)
    rows = [r + [''] * (ncol - len(r)) for r in rows]
    out = []
    for i, r in enumerate(rows):
        out.append('| ' + ' | '.join(r) + ' |')
        if i == 0:
            out.append('|' + '---|' * ncol)
    return '\n'.join(out)

def list_to_md(ul):
    out = []
    is_ol = (ul.name == 'ol')
    idx = 1
    for li in ul.find_all('li', recursive=False):
        # 嵌套列表
        sub = ''
        inner = []
        for ch in li.children:
            if getattr(ch, 'name', None) in ('ul', 'ol'):
                sub = '\n' + list_to_md(ch)
            elif getattr(ch, 'name', None) is not None:
                inner.append(ch.get_text(' ', strip=True))
        txt = clean_text(' '.join(inner)) if inner else clean_text(li.get_text(' ', strip=True))
        if txt:
            prefix = f"{idx}. " if is_ol else '- '
            out.append(prefix + txt)
            idx += 1
        if sub:
            for line in sub.split('\n'):
                out.append('  ' + line)
    return '\n'.join(out)

def convert_body(body):
    """按 DOM 顺序转换 body 内容为 markdown 行列表。"""
    lines = []
    # 递归处理
    def handle(el):
        if getattr(el, 'name', None) is None:
            t = clean_text(el)
            if t:
                lines.append(('para', t))
            return
        name = el.name
        cls = ' '.join(el.get('class') or [])
        if name in ('script', 'style', 'iframe', 'meta', 'link', 'head', 'nav', 'header', 'footer'):
            return
        if name in ('h1',):
            # 标题单独处理
            t = clean_text(el.get_text(' ', strip=True))
            if t:
                lines.append(('h1', t))
            return
        if name in ('h2', 'h3', 'h4', 'h5'):
            t = clean_text(el.get_text(' ', strip=True))
            if t:
                lines.append(('h' + name[1], t))
            return
        if 'MCDropDownHead' in cls:
            t = clean_text(el.get_text(' ', strip=True))
            if t:
                lines.append(('h3', t))
            return
        if name == 'p':
            if is_junk(el):
                return
            if 'note' in cls:
                t = clean_text(el.get_text(' ', strip=True))
                if t:
                    lines.append(('note', t))
                return
            if 'tip' in cls:
                t = clean_text(el.get_text(' ', strip=True))
                if t:
                    lines.append(('tip', t))
                return
            t = clean_text(el.get_text(' ', strip=True))
            if not t or t.startswith('You are here') or t in ('Open topic with navigation',):
                return
            lines.append(('para', t))
            return
        if name == 'table':
            md = table_to_md(el)
            if md:
                lines.append(('table', md))
            return
        if name in ('ul', 'ol'):
            md = list_to_md(el)
            if md:
                lines.append(('list', md))
            return
        if name == 'pre':
            # 去掉行号列，取 code 内容
            for ln in el.find_all('span', class_=lambda c: c and 'codeSnippetLineNumbers' in ' '.join(c)):
                ln.decompose()
            code_el = el.find('code') or el
            # br -> 换行
            for br in code_el.find_all('br'):
                br.replace_with('\n')
            code = code_el.get_text('\n')
            code = re.sub(r'\n{3,}', '\n\n', code).strip('\n')
            if code:
                lines.append(('code', code))
            return
        if name == 'code':
            t = clean_text(el.get_text(' ', strip=True))
            if t:
                lines.append(('inline_code', t))
            return
        if name == 'img':
            alt = (el.get('alt') or '').strip()
            if alt and alt.lower() not in ('closed', 'open', 'show', 'hide', 'expand', 'collapse', 'bullet'):
                lines.append(('para', f'[图片: {alt}]'))
            return
        if name == 'blockquote':
            t = clean_text(el.get_text(' ', strip=True))
            if t:
                lines.append(('note', t))
            return
        if name in ('div', 'section', 'article', 'span', 'a', 'strong', 'em', 'b', 'i', 'br', 'figure', 'figcaption', 'details', 'summary', 'body'):
            # 页脚/面包屑等容器跳过
            if name == 'div':
                low = cls.lower()
                if any(k in low for k in ('footer', 'breadcrumb', 'madcapbodyfooter')) or el.get('id', '').lower() == 'footer':
                    return
            # 容器: 递归子节点
            for ch in el.children:
                handle(ch)
            return
        # 其他未知标签: 取文本
        t = clean_text(el.get_text(' ', strip=True))
        if t:
            lines.append(('para', t))

    # 跳过 body 前的 frameset link 段落
    handle(body)
    return lines

def render(lines, title_override=None):
    out = []
    h1 = None
    for kind, txt in lines:
        if kind == 'h1' and h1 is None:
            h1 = txt
    title = title_override or h1 or ''
    if title:
        out.append(f'# {title}')
        out.append('')
    # 来源由调用方补充
    for kind, txt in lines:
        if kind == 'h1':
            continue
        if kind in ('h2', 'h3', 'h4', 'h5'):
            lvl_map = {'h2': 2, 'h3': 2, 'h4': 3, 'h5': 4}
            lvl = lvl_map.get(kind, 3)
            out.append('#' * lvl + ' ' + txt)
            out.append('')
        elif kind == 'para':
            out.append(txt)
            out.append('')
        elif kind == 'note':
            t = txt
            if t.lower().startswith('note:'):
                t = t[5:].strip()
            out.append('> **Note:** ' + t)
            out.append('')
        elif kind == 'tip':
            t = txt
            if t.lower().startswith('tip:'):
                t = t[4:].strip()
            out.append('> **Tip:** ' + t)
            out.append('')
        elif kind == 'list':
            out.append(txt)
            out.append('')
        elif kind == 'table':
            out.append(txt)
            out.append('')
        elif kind == 'code':
            out.append('```')
            out.append(txt)
            out.append('```')
            out.append('')
        elif kind == 'inline_code':
            out.append(f'`{txt}`')
            out.append('')
    # 去重连续空行
    text = '\n'.join(out)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # 去掉孤立的 "You are here:" 面包屑残留
    text = re.sub(r'^You are here:\s*\n\n?', '', text, flags=re.M)
    return text.strip() + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('url')
    ap.add_argument('-o', '--output', required=True)
    ap.add_argument('--title')
    ap.add_argument('--source', help='来源行显示的 URL')
    args = ap.parse_args()

    if args.url.startswith('http'):
        html = fetch(args.url)
        src_url = args.source or args.url
    else:
        with open(args.url, encoding='utf-8', errors='ignore') as f:
            html = f.read()
        src_url = args.source or args.url

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find('body') or soup
    lines = convert_body(body)
    md = render(lines, args.title)
    title = args.title
    if not title:
        for kind, txt in lines:
            if kind == 'h1':
                title = txt
                break
    # 插入来源行
    if args.source is not None or args.url.startswith('http'):
        hdr = f'> 来源: {src_url}\n\n'
        md = md.replace('\n', '\n', 1)  # no-op
        # 在标题后插入来源
        lines_md = md.split('\n')
        # 找到第一个 # 标题行
        idx = 0
        for i, l in enumerate(lines_md):
            if l.startswith('# '):
                idx = i + 1
                break
        lines_md.insert(idx, '')
        lines_md.insert(idx, f'> 来源: {src_url}')
        md = '\n'.join(lines_md)
        md = re.sub(r'\n{3,}', '\n\n', md)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"OK -> {args.output} ({len(md)} chars, title='{title}')")

if __name__ == '__main__':
    main()
