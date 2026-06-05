require("dotenv").config();

const express = require("express");

const app = express();

app.use(express.json());

const testRoute = require("./routes/testRoute");

app.use("/api", testRoute);

app.listen(process.env.PORT, () => {
    console.log(`Server running on port ${process.env.PORT}`);
});