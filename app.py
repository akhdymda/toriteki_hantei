import streamlit as st
from judge_transaction import judge_transaction

st.title("取適法判定アプリ")

# 取引内容の選択ボックス
st.subheader("取引内容", divider=True)
transaction_type = st.selectbox(
    "取引内容を選択してください",
    ["製造委託","修理委託","情報成果物作成委託（プログラムの作成）", "情報成果物作成委託（プログラムの作成以外）", "役務提供委託（運送，物品の倉庫における保管、情報処理）", "役務提供委託（運送，物品の倉庫における保管、情報処理以外）", "特定運送委託"],
    index=None
)

# 自社の資本金・従業員数の入力
st.subheader("自社情報", divider=True)
own_capital = st.number_input("自社の資本金（円）", value=None, step=1, format="%d", placeholder="例: 100000000")
own_employees = st.number_input("自社の従業員数（人）", value=None, step=1, format="%d", placeholder="例: 100")

# 取引先の資本金・従業員数の入力
st.subheader("取引先情報", divider=True)
partner_capital = st.number_input("取引先の資本金（円）", value=None, step=1, format="%d", placeholder="例: 10000000")
partner_employees = st.number_input("取引先の従業員数（人）", value=None, step=1, format="%d", placeholder="例: 50")

# 判定ボタン
if st.button("判定"):
    if transaction_type is None or own_capital is None or own_employees is None or partner_capital is None or partner_employees is None:
        st.error("すべての情報を入力してください。")
    else:
        result = judge_transaction(transaction_type, own_capital, own_employees, partner_capital, partner_employees)
        st.subheader("判定結果", divider=True)
        if result == "中小受託取引に該当":
            st.success(f"{result}")
            st.info("この取引は下請法の適用対象である可能性があります。")
        else:
            st.warning(f"{result}")
            st.info("この取引は下請法の適用対象ではない可能性があります。")