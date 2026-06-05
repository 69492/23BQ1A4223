const express = require("express");

const router = express.Router();

const logger = require("../middleware/logger");

const { getTest } = require("../controllers/testController");

router.get("/test", logger, getTest);

module.exports = router;