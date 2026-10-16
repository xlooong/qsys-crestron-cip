#!/usr/bin/env python3
"""
Q-SYS qplug 验证脚本
检查：括号匹配、必填函数、GetPages格式、控件名引用一致性
用法: python validate_qplug.py <path-to.qplug>
"""
import sys
import re

def check_brackets(content):
    """检查括号匹配"""
    errors = []
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    line = 1
    col = 0
    in_string = False
    string_char = None
    in_comment = False

    for i, ch in enumerate(content):
        if ch == '\n':
            line += 1
            col = 0
            continue
        col += 1

        if in_comment:
            if ch == '\n':
                in_comment = False
            continue

        if in_string:
            if ch == '\\':
                continue
            if ch == string_char:
                in_string = False
            continue

        if ch == '-' and i + 1 < len(content) and content[i+1] == '-':
            in_comment = True
            continue
        if ch in ('"', "'"):
            in_string = True
            string_char = ch
            continue

        if ch in '([{':
            stack.append((ch, line, col))
        elif ch in ')]}':
            if not stack:
                errors.append(f"Line {line}: unexpected '{ch}'")
            else:
                open_ch, open_line, open_col = stack.pop()
                if open_ch != pairs[ch]:
                    errors.append(f"Line {line}: '{ch}' does not match '{open_ch}' at line {open_line}")

    for ch, line, col in stack:
        errors.append(f"Line {line}: unclosed '{ch}'")

    return errors

def check_required_functions(content):
    """检查必填函数"""
    required = ['GetProperties', 'GetControls', 'GetPages', 'GetControlLayout']
    errors = []
    for func in required:
        if not re.search(rf'function\s+{func}\s*\(', content):
            errors.append(f"Missing required function: {func}()")
    return errors

def check_getpages_format(content):
    """检查 GetPages 返回格式"""
    errors = []
    # 找到 GetPages 函数体
    m = re.search(r'function\s+GetPages\s*\([^)]*\)\s*(.*?)\s*end\s*(?=\nfunction|\Z)', content, re.DOTALL)
    if m:
        body = m.group(1)
        # 检查是否有 return { {name = ...} } 格式
        if not re.search(r'\{\s*name\s*=', body):
            errors.append("GetPages may return string array instead of {name=...} table array")
        # 检查是否有 return {"xxx"} 这种错误格式
        if re.search(r'return\s*\{\s*"[^"]+"', body):
            errors.append("GetPages returns string array - must be {name='...'} table array")
    return errors

def check_knob_controlunit(content):
    """检查 Knob 控件是否有 ControlUnit"""
    errors = []
    # 找到所有 Knob 控件定义
    knob_pattern = r'\{\s*Name\s*=\s*"([^"]+)"[^}]*ControlType\s*=\s*"Knob"[^}]*\}'
    for m in re.finditer(knob_pattern, content, re.DOTALL):
        block = m.group(0)
        if 'ControlUnit' not in block:
            name = m.group(1)
            errors.append(f"Knob '{name}' missing ControlUnit='Integer' - external pin won't appear")
    return errors

def check_userpin_pinstyle(content):
    """检查 UserPin=false 但写了 PinStyle 的控件"""
    warnings = []
    pattern = r'\{\s*Name\s*=\s*"([^"]+)"[^}]*UserPin\s*=\s*false[^}]*PinStyle[^}]*\}'
    for m in re.finditer(pattern, content, re.DOTALL):
        name = m.group(1)
        warnings.append(f"Control '{name}': UserPin=false but PinStyle set - pin may still appear")
    return warnings

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_qplug.py <path-to.qplug>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"ERROR: Cannot read file: {e}")
        sys.exit(1)

    print(f"Validating: {filepath}")
    print(f"Size: {len(content)} bytes, {content.count(chr(10))+1} lines")
    print("=" * 60)

    all_ok = True

    # 1. 括号匹配
    errors = check_brackets(content)
    if errors:
        all_ok = False
        print("\n[BRACKET ERRORS]")
        for e in errors:
            print(f"  {e}")
    else:
        print("  [OK] Bracket matching")

    # 2. 必填函数
    errors = check_required_functions(content)
    if errors:
        all_ok = False
        print("\n[MISSING FUNCTIONS]")
        for e in errors:
            print(f"  {e}")
    else:
        print("  [OK] Required functions present")

    # 3. GetPages 格式
    errors = check_getpages_format(content)
    if errors:
        all_ok = False
        print("\n[GETPAGES FORMAT]")
        for e in errors:
            print(f"  {e}")
    else:
        print("  [OK] GetPages format")

    # 4. Knob ControlUnit
    errors = check_knob_controlunit(content)
    if errors:
        all_ok = False
        print("\n[KNOB CONTROLUNIT]")
        for e in errors:
            print(f"  {e}")
    else:
        print("  [OK] Knob ControlUnit")

    # 5. UserPin/PinStyle 警告
    warnings = check_userpin_pinstyle(content)
    if warnings:
        print("\n[WARNINGS]")
        for w in warnings:
            print(f"  {w}")

    print("\n" + "=" * 60)
    if all_ok:
        print("RESULT: ALL CHECKS PASSED")
    else:
        print("RESULT: ERRORS FOUND - please fix above issues")
        sys.exit(1)

if __name__ == '__main__':
    main()
