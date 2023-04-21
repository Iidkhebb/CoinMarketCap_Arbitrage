import React from 'react'
import Coins from '../pages/Coins'

function Body() {
  return (
	<>
	<div className="body-part">
		<div className='news'>
			<h1>Today's Cryptocurrency Arbitrage  by Profit %</h1>
			<p>The global crypto market cap is $975.16B, a <span class="value-p">0.31%</span> decrease over the last day. <a href='https://coinmarketcap.com/'>Read More</a></p>
		</div>
	</div>

		

	<Coins />


	</>
  )
}

export default Body