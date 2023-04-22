<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="CMC_Arbitrage__V3_0"></a>CMC Arbitrage - V3</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="_Easy_GUI_tool_to_find_prices_gaps_between_crypto_exchanges__1"></a><em>Easy GUI tool to find prices gaps between crypto exchanges</em></h2>
<p class="has-line-data" data-line-start="4" data-line-end="5"><a href="https://travis-ci.org/joemccann/dillinger"><img src="https://travis-ci.org/joemccann/dillinger.svg?branch=master" alt="Build Status"></a></p>
<p class="has-line-data" data-line-start="6" data-line-end="8">CMC Arbitrage - V3  is a web application to help you find the best crypto arbitrage deals<br>
( over 9500 token supported ) between crypto exchanges such as :</p>
<ul>
<li class="has-line-data" data-line-start="8" data-line-end="9">Binance</li>
<li class="has-line-data" data-line-start="9" data-line-end="10">KuCoin</li>
<li class="has-line-data" data-line-start="10" data-line-end="11">LATOKEN</li>
<li class="has-line-data" data-line-start="11" data-line-end="12"><a href="http://Gate.io">Gate.io</a></li>
<li class="has-line-data" data-line-start="12" data-line-end="13">MEXC</li>
<li class="has-line-data" data-line-start="13" data-line-end="14">AAX</li>
<li class="has-line-data" data-line-start="14" data-line-end="15"><a href="http://CEX.IO">CEX.IO</a></li>
<li class="has-line-data" data-line-start="15" data-line-end="16">Huobi Global</li>
<li class="has-line-data" data-line-start="16" data-line-end="17"><a href="http://XT.COM">XT.COM</a></li>
<li class="has-line-data" data-line-start="17" data-line-end="18">Poloniex</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">LBank</li>
<li class="has-line-data" data-line-start="19" data-line-end="20">ShibaSwap</li>
<li class="has-line-data" data-line-start="20" data-line-end="21">OKX</li>
<li class="has-line-data" data-line-start="21" data-line-end="22">PancakeSwap (V2)</li>
<li class="has-line-data" data-line-start="22" data-line-end="23">Hotbit</li>
<li class="has-line-data" data-line-start="23" data-line-end="24">BitMart</li>
</ul>
<h2 class="code-line" data-line-start=28 data-line-end=29 ><a id="Features_28"></a>Features</h2>
<ul>
<li class="has-line-data" data-line-start="30" data-line-end="31">Filtred Scam token using TokenSniffer &amp; Dextools data.</li>
<li class="has-line-data" data-line-start="31" data-line-end="37">A given Audit (Trust) Score with each token genreated using :
<ul>
<li class="has-line-data" data-line-start="32" data-line-end="33">Sentiment analysis data</li>
<li class="has-line-data" data-line-start="33" data-line-end="34">Token audience</li>
<li class="has-line-data" data-line-start="34" data-line-end="35">Social media Followers (Telegram, Twitter …)</li>
<li class="has-line-data" data-line-start="35" data-line-end="36">Coingecko Trust Score</li>
<li class="has-line-data" data-line-start="36" data-line-end="37">Audit certificates</li>
</ul>
</li>
<li class="has-line-data" data-line-start="37" data-line-end="39">The best deals are only displayed if the both exchanges have the enough liquidity to<br>
support a minimum of 1000$ order size.</li>
<li class="has-line-data" data-line-start="39" data-line-end="40">DEX exchanges are supported</li>
<li class="has-line-data" data-line-start="40" data-line-end="41">Only 10% and above profit are displayed to avoid any capital loss.</li>
</ul>
<h2 class="code-line" data-line-start=43 data-line-end=44 ><a id="Tech_43"></a>Tech</h2>
<p class="has-line-data" data-line-start="44" data-line-end="45">CMC Arbitrage V3 uses a number of open source projects to work properly:</p>
<ul>
<li class="has-line-data" data-line-start="46" data-line-end="47">[Python]</li>
<li class="has-line-data" data-line-start="47" data-line-end="48">[ReactJs]</li>
<li class="has-line-data" data-line-start="48" data-line-end="49">[MongoDB]</li>
<li class="has-line-data" data-line-start="49" data-line-end="50">[Celery]</li>
<li class="has-line-data" data-line-start="50" data-line-end="51">[Django]</li>
<li class="has-line-data" data-line-start="50" data-line-end="51">[Redis]</li>
<li class="has-line-data" data-line-start="51" data-line-end="53">[Docker]</li>
</ul>

## Installation

1. Install [Docker](https://www.docker.com/).
2. Clone the repository:

```
git clone https://github.com/Iidkhebb/CoinMarketCap_Arbitrage
cd CoinMarketCap_Arbitrage
```

3. Create a new `.env` file in the project root directory and update the values according to your needs:

```
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1
CELERY_BROKER=redis://redis:6379/0
CELERY_RESULT_BACKEND=mongodb
CELERY_MONGODB_BACKEND_SETTINGS=mongodb://<mongo_user>:<mongo_password>@mongodb:27017
MONGO_HOST=mongodb://<mongo_user>:<mongo_password>@mongodb:27017/CMC
SECRET_KEY=django-insecure-<your_secret_key>
MONGO_INITDB_ROOT_USERNAME=<mongo_root_user>
MONGO_INITDB_ROOT_PASSWORD=<mongo_root_password>
MONGO_INITDB_ROOT_DATABASE=CMC

```

4. Build and start the Docker containers using `docker-compose`:

```
docker-compose up --build
```

OR

```
make
```

5. Open your web browser and navigate to `http://localhost:3000` to access the application.
