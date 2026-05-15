#!/usr/bin/env python3
"""
领克07 EM-P 油耗数据模拟服务
模拟领克APP登录并拉取车辆数据，保存为data.json
提供HTTP API供前端读取
"""

import json
import random
import os
from datetime import datetime, timedelta
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.json")
PORT = 8080

# 模拟车辆基础数据
VEHICLE_INFO = {
    "vin": "LVGHxxxxxx12345",
    "model": "领克07 EM-P",
    "color": "拂晓蓝",
    "plate": "浙A·D12345"
}


def generate_daily_data(days=30):
    """生成近30天的每日油电消耗数据"""
    daily_data = []
    base_date = datetime.now() - timedelta(days=days)
    
    # 初始累计值
    total_fuel_liters = 0
    total_electricity_kwh = 0
    total_mileage = 12580.0  # 初始里程
    
    for i in range(days):
        date = base_date + timedelta(days=i)
        # 模拟每日行驶里程 (10-80km)
        daily_mileage = round(random.uniform(10, 80), 1)
        # 纯电模式占比 60%-90%
        electric_ratio = random.uniform(0.6, 0.9)
        
        # 计算油电消耗
        electric_mileage = daily_mileage * electric_ratio
        fuel_mileage = daily_mileage * (1 - electric_ratio)
        
        # 油耗: 约5-6L/100km (馈电状态)
        fuel_consumption = round(fuel_mileage / 100 * random.uniform(5.0, 6.0), 2)
        # 电耗: 约14-18kWh/100km
        electricity_consumption = round(electric_mileage / 100 * random.uniform(14, 18), 2)
        
        total_fuel_liters += fuel_consumption
        total_electricity_kwh += electricity_consumption
        total_mileage += daily_mileage
        
        daily_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "mileage": daily_mileage,
            "fuel_liters": fuel_consumption,
            "electricity_kwh": electricity_consumption,
            "fuel_cost": round(fuel_consumption * 8.5, 2),  # 油价8.5元/L
            "electricity_cost": round(electricity_consumption * 0.6, 2),  # 电价0.6元/kWh
        })
    
    return daily_data, total_fuel_liters, total_electricity_kwh, total_mileage


def generate_monthly_data(months=6):
    """生成近6个月的月度费用数据"""
    monthly_data = []
    base_date = datetime.now()
    
    for i in range(months):
        date = base_date - timedelta(days=30 * i)
        days_in_month = 30
        
        total_fuel_cost = 0
        total_electricity_cost = 0
        
        for _ in range(days_in_month):
            daily_mileage = random.uniform(15, 70)
            electric_ratio = random.uniform(0.6, 0.9)
            
            fuel_mileage = daily_mileage * (1 - electric_ratio)
            electric_mileage = daily_mileage * electric_ratio
            
            fuel_consumption = fuel_mileage / 100 * random.uniform(5.0, 6.0)
            electricity_consumption = electric_mileage / 100 * random.uniform(14, 18)
            
            total_fuel_cost += fuel_consumption * 8.5
            total_electricity_cost += electricity_consumption * 0.6
        
        monthly_data.append({
            "month": date.strftime("%Y-%m"),
            "fuel_cost": round(total_fuel_cost, 2),
            "electricity_cost": round(total_electricity_cost, 2),
            "total_cost": round(total_fuel_cost + total_electricity_cost, 2)
        })
    
    monthly_data.reverse()
    return monthly_data


def get_vehicle_status():
    """获取车辆当前状态"""
    return {
        "fuel_level": round(random.uniform(35, 75), 1),  # 油量百分比
        "battery_level": round(random.uniform(40, 95), 1),  # 电量百分比
        "fuel_range": round(random.uniform(350, 650), 0),  # 燃油续航km
        "electric_range": round(random.uniform(60, 170), 0),  # 纯电续航km
        "total_range": 0,  # 总续航 = fuel_range + electric_range
        "total_mileage": round(12580 + random.uniform(0, 500), 1),  # 累计里程
        "saved_fuel_cost": round(random.uniform(2800, 3500), 2),  # 累计省油费用
        "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def generate_data():
    """生成完整数据并保存到data.json"""
    daily_data, total_fuel, total_electricity, total_mileage = generate_daily_data(30)
    monthly_data = generate_monthly_data(6)
    vehicle_status = get_vehicle_status()
    
    # 总续航
    vehicle_status["total_range"] = int(vehicle_status["fuel_range"] + vehicle_status["electric_range"])
    
    data = {
        "vehicle": VEHICLE_INFO,
        "status": vehicle_status,
        "daily": daily_data,
        "monthly": monthly_data,
        "summary": {
            "total_mileage": round(total_mileage, 1),
            "total_fuel_liters": round(total_fuel, 2),
            "total_electricity_kwh": round(total_electricity, 2),
            "total_fuel_cost": round(total_fuel * 8.5, 2),
            "total_electricity_cost": round(total_electricity * 0.6, 2),
            "saved_fuel_cost": vehicle_status["saved_fuel_cost"],
            "last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 数据已更新: {DATA_FILE}")
    return data


class DashboardHandler(SimpleHTTPRequestHandler):
    """自定义HTTP处理器"""
    
    def do_GET(self):
        if self.path == "/api/data" or self.path == "/api/data/":
            self.send_cors_headers()
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            else:
                self.wfile.write(json.dumps({"error": "数据文件不存在"}).encode("utf-8"))
        
        elif self.path == "/api/refresh" or self.path == "/api/refresh/":
            self.send_cors_headers()
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            
            data = generate_data()
            self.wfile.write(json.dumps({"status": "ok", "update_time": data["summary"]["last_update"]}).encode("utf-8"))
        
        else:
            # 提供静态文件
            if self.path == "/" or self.path == "/index.html":
                self.path = "/index.html"
            return super().do_GET()
    
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")


def auto_refresh():
    """每30分钟自动刷新数据"""
    while True:
        threading.Timer(1800, auto_refresh).start()  # 30分钟 = 1800秒
        generate_data()


def main():
    # 首次生成数据
    print("=" * 50)
    print("  领克07 EM-P 油耗可视化看板")
    print("=" * 50)
    generate_data()
    
    # 启动自动刷新
    auto_refresh()
    
    # 启动HTTP服务
    server = HTTPServer(("0.0.0.0", PORT), DashboardHandler)
    print(f"\n✓ 服务已启动: http://localhost:{PORT}")
    print(f"✓ 数据文件: {DATA_FILE}")
    print(f"✓ 自动刷新: 每30分钟")
    print(f"✓ 按 Ctrl+C 停止服务\n")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止")
        server.server_close()


if __name__ == "__main__":
    main()
