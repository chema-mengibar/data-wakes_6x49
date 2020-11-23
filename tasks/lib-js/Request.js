const fs = require("fs");
const axios = require("axios");

const secret = require("../secret/secret");

function createHeaders(host) {
  return {
    Accept:
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    Host: host, // host example: "motuo.example.info"
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    Connection: "keep-alive",
    "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0",
    "Content-Type": "application/json",
  };
}

function request(host, url, cookie, method = "get") {
  const basicHeaders = createHeaders(host);
  return axios.request({
    url: url,
    method: method,
    headers: {
      ...basicHeaders,
      Cookie: cookie,
    },
  });
}

exports.request = request;
