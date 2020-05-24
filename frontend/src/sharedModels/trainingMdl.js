import trainingApi from "../sharedApis/trainingApi"

export const getAllTrainingRequest = async () => {
  try {
    const fetch = await trainingApi.getAll();
    const response = await fetch.json()
    return response;
  } catch (error) {
    return {
      status: {
        code: 500,
        error: error,
        message: `Internal server error.`
      }
    }
  }
}