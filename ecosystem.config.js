module.exports = {
    apps: [
        {
            name: "tg-gifts-bot",
            script: "./main.py",
            interpreter: "./.venv/bin/python3",
            cwd: "/root/scripts/tg-gifts-bot",
            watch: false,
            error_file: "/root/.pm2/logs/tg-gifts-bot-error.log",
            out_file: "/root/.pm2/logs/tg-gifts-bot-out.log",
            pid_file: "/root/.pm2/pids/tg-gifts-bot.pid",
            exec_mode: "fork",
            env: {
                NODE_ENV: "production",
            },
            log_date_format: "YYYY-MM-DD HH:mm:ss",
            max_size: "10M",
            merge_logs: true,
            // cron_restart: "0 6 * * *", // Убрано, чтобы скрипт никогда не перезапускался
            autorestart: false
        },
    ],
};