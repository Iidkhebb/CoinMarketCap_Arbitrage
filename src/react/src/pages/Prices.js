import React, { useState, useEffect } from "react";

function Prices() {
  let [pricesquery, setprices] = useState([]);

  useEffect(() => {
    setInterval(async () => {
      data();
    }, 10000);
  }, []);

  let data = async () => {
    let res = await fetch("/api/getFeedBar");
    let parse = await res.json();
    console.log(parse);
    setprices(parse);
  };

  return (
    <div>
      <nav className="bar">
        <ul>
          {pricesquery.map((item) => {
            return (
              <li key={item.id}>
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>Cryptos</span>{" "}
                  : {item.cryptos}
                </span>
                {"  "}
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>Exchanges</span>{" "}
                  : {item.exchanges}
                </span>
                {"  "}
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>
                    Marketcap
                  </span>{" "}
                  : {item.marketcap}
                </span>
                {"  "}
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>Volume</span>{" "}
                  : {item.volume}
                </span>
                {"  "}
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>Dominance</span>{" "}
                  : {item.dominance}
                </span>
                {"  "}
                <span>
                  <span style={{ color: "rgb(161, 167, 187)" }}>ETH Gas</span>{" "}
                  : {item.ethgas}
                </span>
              </li>
            );
          })}

          <span class="lang">English</span>
          <span class="curr">USD</span>

          <span class="far fa-sun"></span>
          <span class="wall"></span>
          <button className="login-btn">login</button>
          <button className="signup-btn">signup</button>
        </ul>
      </nav>
    </div>
  );
}

export default Prices;
