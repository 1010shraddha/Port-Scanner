from flask import Flask, render_template, request
from scanner import scan_ports
import socket
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    scan_time = None
    target = None
    resolved_ip = None
    total_ports = 0
    risk = "N/A"

    if request.method == "POST":

        target = request.form["target"]
        start_port = int(request.form["start_port"])
        end_port = int(request.form["end_port"])

        total_ports = end_port - start_port + 1

        try:
            resolved_ip = socket.gethostbyname(target)
        except:
            resolved_ip = "Unable to Resolve"

        start = time.time()

        results = scan_ports(
            target,
            start_port,
            end_port
        )

        scan_time = round(time.time() - start, 2)

        open_ports_count = len(results)

        if open_ports_count <= 5:
            risk = "Low"
        elif open_ports_count <= 15:
            risk = "Medium"
        else:
            risk = "High"

    return render_template(
        "index.html",
        results=results,
        scan_time=scan_time,
        target=target,
        resolved_ip=resolved_ip,
        total_ports=total_ports,
        risk=risk
    )

if __name__ == "__main__":
    app.run(debug=True)