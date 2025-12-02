st.data_editor(df, column_config={
    "price": st.column_config.NumberColumn(
        "가격", min_value=0, max_value=100000, format="₩%.0f")
})