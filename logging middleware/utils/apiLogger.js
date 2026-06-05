const axios = require("axios");

async function apiLogger(stack, level, packageName, message) {
    try {
        await axios.post(
            process.env.LOG_API,
            {
                stack,
                level,
                package: packageName,
                message
            },
            {
                headers: {
                    Authorization: `Bearer ${process.env.ACCESS_TOKEN}`,
                    "Content-Type": "application/json"
                }
            }
        );
    } catch (error) {
        console.log(error.message);
    }
}

module.exports = apiLogger;