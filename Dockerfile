FROM frappe/bench:latest

# Set working directory inside bench
WORKDIR /home/frappe/frappe-bench

# Copy only your custom apps (not the whole bench)
COPY apps/ /home/frappe/frappe-bench/apps/

# Expose default Frappe port
EXPOSE 8000

# Start Frappe web service
CMD ["bench", "start"]
