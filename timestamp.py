from datetime import datetime

def convert_timestamp(timestamp):
    """
    タイムスタンプから必要な変数を計算する関数。

    Args:
        timestamp (str): 現在の時刻（YYYY-MM-DD HH:MM:SS形式）。

    Returns:
        dict: 変換された値を含む辞書。
    """
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

        # 1. day: 3月1日から数えて何日目か
        start_of_year = datetime(dt.year, 3, 1)
        if dt.month < 3:  # 年をまたぐ場合の調整
            start_of_year = datetime(dt.year - 1, 3, 1)
        day = (dt - start_of_year).days 

        # 2. hm: 1日を3分刻みで数値化
        minutes_in_day = dt.hour * 60 + dt.minute
        hm = minutes_in_day // 3

        # 3. s: 3分以下を秒数で数値化する
        s = minutes_in_day % 3 * 60 + dt.second

        # 4. mo: 2001年1月から何か月経過したか
        mo = (dt.year - 2001) * 12 + dt.month - 1

        # 5. h: 毎月1日午前0時から2時間ごとでどれだけ経過したか
        start_of_month = datetime(dt.year, dt.month, 1)
        hours_since_start_of_month = (dt - start_of_month).total_seconds() // (2 * 3600)
        h = int(hours_since_start_of_month)

        # 6. mi: 現在時刻からhを引いた値を15秒単位で計算
        current_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second  # 現在時刻を秒に変換
        remaining_seconds = current_seconds % 7200  # 7200秒（2時間）で割った余り
        mi = remaining_seconds // 15  # 15秒で割った値

        # 7. ss: 15秒を0.05ms単位で分割した数字
        ss = int((remaining_seconds % 15) / 0.05)

        # 結果を辞書で返す
        return {
            "day": day,
            "hm": hm,
            "s": s,
            "mo": mo,
            "h": h,
            "mi": mi,
            "ss": ss
        }

    except Exception as e:
        print(f"Error converting timestamp: {e}")
        return {}

def main():
    print("タイムスタンプ変換プログラム")
    print("========================")
    
    # PCの現在時刻を自動的に取得
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"現在時刻を使用します: {timestamp}")
    
    try:
        result = convert_timestamp(timestamp)
        print("\n変換結果:")
        for key, value in result.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
