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