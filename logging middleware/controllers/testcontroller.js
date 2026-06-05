const apiLogger = require("../utils/apiLogger");

const getTest = async (req, res) => {
    try {
        await apiLogger(
            "backend",
            "info",
            "controller",
            "Test API called"
        );

        res.status(200).json({
            success: true,
            message: "Logging middleware working"
        });
    } catch (error) {
        await apiLogger(
            "backend",
            "error",
            "controller",
            error.message
        );

        res.status(500).json({
            success: false,
            message: "Server Error"
        });
    }
};

module.exports = { getTest };