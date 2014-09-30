getDoorkeeperExcel
===============

Selenium経由でdoorKeeperのExcelを落としてくる。
CUIで実行可能なため、LinuxのCronで実行出来る。

# 実行環境の構築例（Ubuntu 14.04.1 LTS)
※さくらクラウドのUbuntu 14.04.1 LTSのアーカイブインストールで確認

    # sudo apt-get install firefox
    # sudo apt-get install xvfb
    # sudo apt-get install python-pip
    # sudo pip install selenium
    # pip install pyvirtualdisplay
    
# アプリケーションの実行
    driver.find_element_by_id("user_email").send_keys("change_mail_address")
    21行目のchange_mail_addressをログインで利用するメールアドレスに変更
    
    driver.find_element_by_id("user_password").send_keys("change_password")
    24行目のchange_passwordをログインで利用するパスワードに変更
    
    driver.get("change_url")
    27行目のchange_urlを実際にダウンロードするExcelのURLに変更
    ※例　https://manage.doorkeeper.jp/groups/hoge/events/99999999/tickets.xlsx

    # /usr/bin/python getDoorkeeperExcel.py
    
##doorKeeperの参加者一覧ExcelをWebのTableで表示する場合
[viewExcel2Table](https://github.com/soudai/viewExcel2Table) 