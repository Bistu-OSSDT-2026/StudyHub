# StudyHub
Team-17
StudyHub - 自习室预约系统
北京信息科技大学 · 开源软件开发技术 · 课程实践3
项目简介
StudyHub 是一个基于 Web 的自习室座位预约管理系统。学生可以在线浏览自习室、查看座位实时状态、提交预约和取消预约；管理员可以管理自习室信息、查看预约记录和数据统计。
系统采用前后端分离架构，前端使用 Vue3 + Element Plus 构建 SPA，后端使用 Python Flask 提供 RESTful API，开发期使用 SQLite 数据库，可平滑切换至 MySQL。
功能特性
自习室浏览：查看所有可用自习室及其开放时间
座位管理：实时查看座位状态（空闲/已占用），按楼层筛选
座位预约：选择时间段提交预约，自动检测时间冲突
取消预约：支持取消已有预约，释放座位资源
数据统计：可视化展示各自习室使用率和预约趋势
响应式设计：适配桌面和平板设备

技术栈
前端	Vue 3 + Vite + Element Plus + Axios
后端	Python 3.10+ + Flask + Flask-CORS
后端	Python 3.10+ + Flask + Flask-CORS
数据可视化	ECharts 5
协作托管	GitHub

项目结构
StudyHub/
├── backend/                # 后端服务
│   ├── app.py             # Flask 应用主入口
│   ├── config.py          # 配置文件
│   ├── models.py          # 数据模型（SQLAlchemy）
│   ├── init_db.py         # 数据库初始化脚本
│   ├── requirements.txt   # Python 依赖
│   └── routes/            # API 路由
│       ├── rooms.py       # 自习室接口
│       ├── seats.py       # 座位接口
│       ├── bookings.py    # 预约接口
│       └── stats.py       # 统计接口
├── frontend/              # 前端应用
│   ├── src/
│   │   ├── App.vue       # 根组件
│   │   ├── main.js       # 入口文件
│   │   ├── api/          # API 请求封装
│   │   │   └── index.js
│   │   ├── router/       # 路由配置
│   │   │   └── index.js
│   │   └── views/        # 页面组件
│   │       ├── Home.vue
│   │       ├── Rooms.vue
│   │       ├── RoomDetail.vue
│   │       ├── MyBookings.vue
│   │       └── Stats.vue
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── .github/
│   └── workflows/        # CI/CD 配置
│       └── ci.yml
├── LICENSE
└── README.md



快速开始
环境要求
Python 3.10 或更高版本
Node.js 16 或更高版本
npm 或 yarn

后端启动
# 进入后端目录
cd backend

# 创建并激活虚拟环境（Windows）
python -m venv venv
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 初始化数据库（首次运行）
python init_db.py

# 启动后端服务
python app.py

后端服务将在 http://127.0.0.1:5000 启动。

前端启动
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
前端将在 http://localhost:3000/ 启动，API 请求自动代理到后端 5000 端口。

访问系统
浏览器打开 http://localhost:3000/，即可看到自习室预约系统首页。

API 接口
方法	         路径	                      说明
GET	          /api/rooms	                获取所有自习室
GET	         /api/rooms/:id	              获取自习室详情
GET	         /api/seats?room_id=X	        获取指定自习室的座位
GET	         /api/seats/:id/status	      查询座位某时段状态
POST	       /api/bookings	              创建预约
GET	         /api/bookings?user=X	        查询用户预约
DELETE	     /api/bookings/:id	          取消预约
GET	         /api/stats/usage	            使用率统计

开发规范
分支策略：main 为稳定分支，功能开发从 main 创建 feature/xxx 分支
提交规范：遵循 Conventional Commits（feat: / fix: / docs: / refactor:）
代码审查：所有变更必须通过 Pull Request，至少 1 人 Review 后方可合并
Issue 管理：Bug 报告和功能需求统一通过 GitHub Issues 跟踪

开源协议
本项目仅供北京信息科技大学"开源软件开发技术"课程教学使用。
