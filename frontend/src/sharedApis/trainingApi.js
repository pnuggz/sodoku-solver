import config from "../config";

const baseUrl = config.fmTraining.baseUrl;
const apiKey = config.fmTraining.apiKey;

const getAll = (gameVer=null) => {
  const request = (gameVer) ? `game=${gameVer}` : ``
  const url = baseUrl + `/training-modifiers/get?${request}`;

  return fetch(url, {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${apiKey}`,
      "Content-Type": "application/json"
    }
  });
};

const trainingApi = {
  getAll: getAll
};

export default trainingApi;
