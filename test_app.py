import pytest

def judge_transaction(transaction_type, own_capital, own_employees, partner_capital, partner_employees):
    """
    取引が中小受託取引に該当するかを判定する関数
    """
    result = "中小受託取引に非該当"  # デフォルトを非該当にする

    type1_transactions = ["製造委託", "修理委託", "特定運送委託", "情報成果物作成委託（プログラムの作成）"]
    type2_transactions = ["情報成果物作成委託（プログラムの作成以外）", "役務提供委託"]

    if transaction_type in type1_transactions:
        if own_capital > 300_000_000:
            if partner_capital <= 300_000_000:
                result = "中小受託取引に該当"
            else:  # partner_capital > 300_000_000
                if own_employees > 300 and partner_employees <= 300:
                    result = "中小受託取引に該当"
                else:
                    result = "中小受託取引に非該当"
        elif 10_000_000 < own_capital <= 300_000_000:
            if partner_capital <= 10_000_000:
                result = "中小受託取引に該当"
            else:  # partner_capital > 10_000_000
                if own_employees > 300 and partner_employees <= 300:
                        result = "中小受託取引に該当"
                else:
                        result = "中小受託取引に非該当"
        else:
            result = "中小受託取引に非該当"

    elif transaction_type in type2_transactions:
        if own_capital > 50_000_000:
            if partner_capital <= 50_000_000:
                result = "中小受託取引に該当"
            else:  # partner_capital > 50_000_000
                if own_employees > 100 and partner_employees <= 100:
                    result = "中小受託取引に該当"
                else:
                    result = "中小受託取引に非該当"
        elif 10_000_000 < own_capital <= 50_000_000:
            if partner_capital <= 10_000_000:
                result = "中小受託取引に該当"
            else:  # partner_capital > 10_000_000
                if own_employees > 100 and partner_employees <= 100:
                    result = "中小受託取引に該当"
                else:
                    result = "中小受託取引に非該当"
        else:
            result = "中小受託取引に非該当"
            
    return result

# 「該当」となるパターンのテスト
@pytest.mark.parametrize("transaction_type, own_capital, own_employees, partner_capital, partner_employees, expected", [
    # --- パターン1: 製造委託等、自社資本金3億超 ---
    ("製造委託", 300_000_001, 301, 300_000_000, 300, "中小受託取引に該当"),  # 1-1
    ("製造委託", 300_000_001, 301, 300_000_001, 300, "中小受託取引に該当"),  # 1-2 (従業員数で判定)
    # --- パターン2: 製造委託等、自社資本金1000万超3億以下 ---
    ("修理委託", 300_000_000, 301, 10_000_000, 300, "中小受託取引に該当"),  # 3
    ("修理委託", 300_000_000, 301, 10_000_001, 300, "中小受託取引に該当"),  # 4 (従業員数で判定)
    # --- パターン3: 情報成果物作成委託(プログラム以外)等、自社資本金5000万超 ---
    ("役務提供委託", 50_000_001, 101, 50_000_000, 100, "中小受託取引に該当"), # 5
    ("役務提供委託", 50_000_001, 101, 50_000_001, 100, "中小受託取引に該当"), # 6 (従業員数で判定)
    # --- パターン4: 情報成果物作成委託(プログラム以外)等、自社資本金1000万超5000万以下 ---
    ("情報成果物作成委託（プログラムの作成以外）", 50_000_000, 101, 10_000_000, 100, "中小受託取引に該当"), # 7
    ("情報成果物作成委託（プログラムの作成以外）", 50_000_000, 101, 10_000_001, 100, "中小受託取引に該当"), # 8 (従業員数で判定)
])
def test_judge_transaction_applicable(transaction_type, own_capital, own_employees, partner_capital, partner_employees, expected):
    assert judge_transaction(transaction_type, own_capital, own_employees, partner_capital, partner_employees) == expected

# 「非該当」となるパターンのテスト
@pytest.mark.parametrize("transaction_type, own_capital, own_employees, partner_capital, partner_employees, expected", [
    # --- パターン1: 製造委託等、自社資本金3億超、従業員数で非該当 ---
    ("製造委託", 300_000_001, 300, 300_000_001, 301, "中小受託取引に非該当"), # 自社従業員数が300人以下
    ("製造委託", 300_000_001, 301, 300_000_001, 301, "中小受託取引に非該当"), # 両社の従業員数が300人超
    # --- パターン2: 製造委託等、自社資本金1000万以下 ---
    ("修理委託", 10_000_000, 301, 10_000_000, 300, "中小受託取引に非該当"),
    # --- パターン3: 情報成果物作成委託(プログラム以外)等、自社資本金5000万超、従業員数で非該当 ---
    ("役務提供委託", 50_000_001, 100, 50_000_001, 101, "中小受託取引に非該当"), # 自社従業員数が100人以下
    ("役務提供委託", 50_000_001, 101, 50_000_001, 101, "中小受託取引に非該当"), # 両社の従業員数が100人超
    # --- パターン4: 情報成果物作成委託(プログラム以外)等、自社資本金1000万以下 ---
    ("情報成果物作成委託（プログラムの作成以外）", 10_000_000, 101, 10_000_000, 100, "中小受託取引に非該当"),
])
def test_judge_transaction_not_applicable(transaction_type, own_capital, own_employees, partner_capital, partner_employees, expected):
    assert judge_transaction(transaction_type, own_capital, own_employees, partner_capital, partner_employees) == expected