const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

app.get('/run-model', async (req, res) => {
  try {
    const response = await axios.get('http://python-model:5000/run-model');
    const { accuracy, report } = response.data;

    const output = `Accuracy: ${accuracy}\n${report}`;
    res.send(`<pre>${output}</pre>`);
  } catch (error) {
    console.error("Execution error:", error.message);
    res.status(500).send("Model execution failed");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});