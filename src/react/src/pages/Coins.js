import React, { useState, useEffect } from "react";
import ArrowDropUpIcon from "@mui/icons-material/ArrowDropUp";
import ArrowDropDownIcon from "@mui/icons-material/ArrowDropDown";
import { CopyToClipboard } from "react-copy-to-clipboard";
import Tooltip from "@mui/material/Tooltip";
import IconButton from "@mui/material/IconButton";
import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import { useLocation } from "react-router-dom";

function Coins() {
  const [current, setCurrent] = useState(0);
  const [dropdown, setDropdown] = useState(false);

  let DropDown = () => {
    function useQuery() {
      const { search } = useLocation();

      return React.useMemo(() => new URLSearchParams(search), [search]);
    }
    let query = useQuery();
    const active = query.get("chain");
    const handleClick = (index) => {
      setCurrent(index);
      setDropdown(!dropdown);
    };
  };

  let [dataraw, setdataraw] = useState([]);
  const [copie, setcopie] = useState(false);
  const styles = {
    heigh: {
      background: "linear-gradient(145deg, #3afd61, #31d452);",
      boxShadow:
        "rgb(19 255 65 / 22%) 5px 5px 20px, rgb(19 255 65 / 22%) -5px -5px 20px",
      borderRadius: "43px",
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    scam: {
      background: "linear-gradient(145deg, #3afd61, #31d452);",
      boxShadow:
        "rgb(255 17 109 / 22%) 5px 5px 20px, rgb(240 131 186 / 22%) -5px -5px 20px",
      borderRadius: "43px",
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    moderate: {
      backgroundColor: "#ffcc00",
      borderRadius: 50,
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    low: {
      backgroundColor: "grey",
      borderRadius: 50,
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    noLiquidity: {
      backgroundColor: "belgrey",
      borderRadius: 50,
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    LowThanLow: {
      backgroundColor: "#ECF2FF",
      borderRadius: 50,
      textAlign: "center",
      display: "block",
      width: "0px",
      height: "0px",
      marginTop: "17px",
      marginLeft: "19px",
    },
    dropactivate: {},
  };

  useEffect(() => {
    setInterval(async () => {
      const res = await fetch(`/api/getAbitrageDeals`);
      const data = await res.json();
      setdataraw(data);
    }, 3000);
  }, []);

  useEffect(() => {
    setInterval(() => {
      setcopie(false);
    }, 8000);
  }, []);

  return (
    <div className="coins">
      <table cellspacing="25" cellpadding="2">
        <tr className="head">
          <th>#</th>
          <th>Name</th>
          <th>Profit</th>
          <th>Blockchain</th>

          <th>
            Exchange <ArrowDropDownIcon style={{ color: "red" }} />
          </th>

          <th>
            Exchange <ArrowDropUpIcon style={{ color: "lightgreen" }} />
          </th>
          <th>Price Low</th>
          <th>Price High</th>
          <Tooltip
            TransitionProps={{ timeout: 600 }}
            title="A measure of how much of a cryptocurrency was audited by tokensniffer, Dextools, Traded volume, Sentiments score and more."
          >
            <th>
              Audit <i class="fas fa-info-circle"></i>
            </th>
          </Tooltip>
        </tr>

        {dataraw.map((coin) => {
          return (
            <>
              <tr className="rows-s">
                <td>
                  <img
                    style={{
                      borderRadius: 50,
                      margin: "auto",
                      boxShadow:
                        "rgb(74 79 96) 5px 5px 20px, rgb(74 79 96) -5px -5px 20px",
                    }}
                    width="30"
                    src={coin.img_path}
                    alt={coin.address}
                  />
                </td>
                <td>
                  <CopyToClipboard
                    onCopy={() => setcopie(true)}
                    text={coin.address}
                  >
                    <Tooltip
                      TransitionProps={{ timeout: 300 }}
                      title={copie ? "Copied" : "Copy Adress"}
                    >
                      <IconButton
                        style={{
                          fontWeight: "bold",
                          fontSize: "14px",
                          color: "white",
                        }}
                      >
                        {coin.display_name}
                      </IconButton>
                    </Tooltip>
                  </CopyToClipboard>
                </td>
                <td>{coin.diff} %</td>
                <td>{coin.blockchain}</td>
                <td>{coin.exchangeName_low}</td>
                <td>{coin.exchangeName_high}</td>
                <td style={{ fontWeight: "bold", color: "#ea3943" }}>
                  {coin.price_low}
                </td>
                <td style={{ fontWeight: "bold", color: "#16c784" }}>
                  {coin.price_high}
                </td>
                <Tooltip TransitionProps={{ timeout: 400 }} title={coin.audit}>
                  <td
                    style={
                      coin.audit === "High"
                        ? styles.heigh
                        : coin.audit === "Scam"
                        ? styles.scam
                        : coin.audit === "Moderate"
                        ? styles.moderate
                        : coin.audit === "Low"
                        ? styles.low
                        : coin.audit === "No liquidity"
                        ? styles.noLiquidity
                        : coin.audit === "N/A"
                        ? styles.LowThanLow
                        : null
                    }
                  ></td>
                </Tooltip>

                <td>
                  <div onClick={() => setDropdown(!dropdown)}>
                    <div className="left_section">
                      <div>
                        <KeyboardArrowDownIcon
                          style={{
                            color: "white",
                            fontSize: "30px",
                            cursor: "pointer",
                          }}
                        />
                      </div>
                    </div>
                  </div>
                </td>
              </tr>
            </>
          );
        })}
      </table>
    </div>
  );
}

export default Coins;
