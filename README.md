# TradingSystem
TradingSystem TDD KATA

관련 자료: https://drive.google.com/file/d/1OVE4xzTw9xxoFWqulPXsAl255bHiAwZk/view


제공되는 API

✓Nemo증권과 Kiwer증권사에서 제공되는 주식거래 API
▪ 사내 Github : https://github.samsungds.net/cra1-sec/TradingSystem
▪ 사외 Github : https://github.com/mincoding1/TradingSystem
✓KiwerStock
▪ login( ID, PASS )
▪ buy( 종목코드, 수량, 가격 )
▪ sell( 종목코드, 수량, 가격 )
▪ current_price( 종목코드 )

✓NemoStock
▪ certification( ID, PASS )
▪ purchasing_stock( 종목코드, 가격, 수량 )
▪ selling_stock( 종목코드, 가격, 수량 )
▪ get_market_price (종목코드, 시간 )

개발해야 하는 Application - 1

✓자동 매매 프로그램
▪ 증권사 선택 기능 : select_stock_brocker( )
• 키워 or 네모 증권 선택 가능

▪ 로그인 기능 : login(id, pass)
▪ 매수 기능 : buy(종목코드, 가격, 수량)
▪ 매도 기능 : sell(종목코드, 가격, 수량)
▪ 현재가 확인 기능 : get_price(종목코드)

개발해야 하는 Application - 2

✓자동 매매 프로그램
▪ 기능 1 : buy_nice_timing(종목, 금액)
• 가격이 올라가는 추세라면,
사용자가 걸어놓은 금액에 최대 수량만큼 매수한다.
• 현재가 기준으로 매수한다.

▪ 기능 2 : sell_nice_timing(종목, 수량)
• 가격이 내려가는 추세라고 판단되면,
사용자가 설정한 수량만큼 주식을 모두 매도한다.
• 현재가 기준으로 매도한다.