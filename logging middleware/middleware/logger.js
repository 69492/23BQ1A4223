const apiLogger = require("../utils/apiLogger");

const logger = async (req, res, next) => {
    await apiLogger(
        "backend",
        "info",
        "middleware",
        `${req.method} ${req.originalUrl}`
    );

    next();
};

module.exports = logger;