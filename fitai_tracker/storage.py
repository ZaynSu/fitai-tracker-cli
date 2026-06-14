"""
storage.py —— 数据存储模块

职责：
- 管理 ~/.workout-tracker/ 目录下的所有 JSON 文件
- 提供 Profile / Workout / Analysis 的存取接口
- 不关心数据内容——只管"存"和"取"
"""

import json
from pathlib import Path


# ===== 路径常量 =====
DATA_DIR = Path.home() / ".workout-tracker"
PROFILE_FILE = DATA_DIR / "profile.json"
WORKOUTS_DIR = DATA_DIR / "workouts"
ANALYSES_DIR = DATA_DIR / "analyses"


def _ensure_dirs():
    """确保所有数据目录存在——内部函数（不对外暴露）"""
    DATA_DIR.mkdir(exist_ok=True)
    WORKOUTS_DIR.mkdir(exist_ok=True)
    ANALYSES_DIR.mkdir(exist_ok=True)
    # ===== Profile 操作 =====

def save_profile(profile: dict) -> None:
    """
    保存用户档案到 profile.json

    参数：
        profile: 用户档案字典（必须包含 name / age / gender / 等字段）

    副作用：
        - 自动创建 ~/.workout-tracker/ 目录（如不存在）
        - 覆盖写入 profile.json
    """
    _ensure_dirs()
    PROFILE_FILE.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def load_profile() -> dict | None:
    """
    读取用户档案

    返回：
        - 档案字典（如果 profile.json 存在）
        - None（如果用户从未初始化档案）
    """
    if not PROFILE_FILE.exists():
        return None
    return json.loads(PROFILE_FILE.read_text(encoding="utf-8"))
# ===== Workout 操作 =====

def save_workout(workout: dict) -> None:
    """
    保存单次训练记录

    参数：
        workout: 训练字典——必须包含 workout_id 字段

    副作用：
        写入 workouts/{workout_id}.json
    """
    _ensure_dirs()
    workout_id = workout["workout_id"]
    file_path = WORKOUTS_DIR / f"{workout_id}.json"
    file_path.write_text(
        json.dumps(workout, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def load_workout(workout_id: str) -> dict | None:
    """
    根据 ID 读取单次训练记录

    参数：
        workout_id: 训练 ID（如 "20260614-001"）

    返回：
        训练字典 / None（如果不存在）
    """
    file_path = WORKOUTS_DIR / f"{workout_id}.json"
    if not file_path.exists():
        return None
    return json.loads(file_path.read_text(encoding="utf-8"))


def list_workouts() -> list[dict]:
    """
    列出所有训练记录——按日期倒序（最新的在前）

    返回：
        训练字典列表（可能为空）
    """
    if not WORKOUTS_DIR.exists():
        return []
    
    workouts = []
    for file_path in WORKOUTS_DIR.glob("*.json"):
        workout = json.loads(file_path.read_text(encoding="utf-8"))
        workouts.append(workout)
    
    # 按 workout_id 倒序——因为 workout_id 包含日期（"20260614-001"）
    workouts.sort(key=lambda w: w["workout_id"], reverse=True)
    return workouts


def find_last_workout_by_part(part: str) -> dict | None:
    """
    查找最近一次包含指定部位的训练

    参数：
        part: 训练部位（如 "胸" / "背"）

    返回：
        最近一次该部位的训练 / None（如果从未练过）
    """
    all_workouts = list_workouts()  # 已经按日期倒序
    for workout in all_workouts:
        if part in workout.get("target_parts", []):
            return workout
    return None
# ===== Analysis 操作 =====

def save_analysis(analysis: dict) -> None:
    """
    保存训练分析结果

    参数：
        analysis: 分析字典——必须包含 workout_id 字段
                  （和它分析的 workout 用相同 ID——便于关联）

    副作用：
        写入 analyses/{workout_id}.json
    """
    _ensure_dirs()
    workout_id = analysis["workout_id"]
    file_path = ANALYSES_DIR / f"{workout_id}.json"
    file_path.write_text(
        json.dumps(analysis, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


def load_analysis(workout_id: str) -> dict | None:
    """
    根据 workout_id 读取对应的分析结果

    参数：
        workout_id: 训练 ID

    返回：
        分析字典 / None（如果未分析过）
    """
    file_path = ANALYSES_DIR / f"{workout_id}.json"
    if not file_path.exists():
        return None
    return json.loads(file_path.read_text(encoding="utf-8"))