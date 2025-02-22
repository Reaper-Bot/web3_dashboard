  # WEB3_CUSTOM_DASHBOARD
This repo is contain some source code that i use to build personal web3 management task

## Description

I Just try to make my personal web3 management task with deploy at my own server

## Getting Started

## Project Planning & Setup

Before coding, let's define the backend architecture.
1.1 Define Backend Tech Stack

Since you’re using Python (Flask) for Web3, here’s the recommended stack:

   * Flask – Lightweight web framework.
   * SQLAlchemy – ORM for database management.
   * Celery – Task scheduling & automation.
   * Web3.py – Interact with blockchain.
   * JWT (PyJWT) – Authentication & security.
   * PostgreSQL/MySQL – Database for storing tasks & Web3 interactions.
   *  Redis – Message broker for Celery (optional but recommended).

## Backend Environment Setup

 ### Dependencies
```
* mkdir web3_dashboard
* cd web3_dashboard
* python3 -m venv venv
* source venv/bin/activate  # (On Windows: venv\Scripts\activate)
* pip install flask flask-jwt-extended flask-sqlalchemy web3 celery redis
```
### Database Design
Define tables for:
* Tasks (ID, Name, Status, Priority, Web3 Contract Address, etc.)
* Projects (Different Web3 testnet projects)
* Users (Multi-user support, roles, authentication)

  ### Create Models
  Create models at models.py
  
### Implement Authentication (JWT)
 Setup User Authentication (auth.py)
### Task Management API
Create Task Endpoints (task_routes.py)
### Web3 Integration
Setup Web3 Connection (web3_utils.py) 
### Automate Task Status with Celery
* Install celery
```
pip install celery
```
* Run celery
 ```
  celery -A tasks worker --loglevel=info
  ```
### Deployment & Security
```
pip install gunicorn
gunicorn -w 4 app:app
```
### Setup Reverse Proxy (NGINX)

## SETUP FRONTEND

Let's start by setting up Next.js with Tailwind CSS.
🛠 Install Next.js & Dependencies

Run the following:

npx create-next-app@latest web3-dashboard
cd web3-dashboard
npm install tailwindcss @shadcn/ui @wagmi/core viem

📌 Configure Tailwind CSS

Run:
```
npx tailwindcss init -p
```
Modify tailwind.config.js:
```
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./pages/**/*.{js,ts,jsx,tsx}", "./components/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};
```
✅ Now your frontend project is ready!
### Build the UI Layout
```
import { useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { useAccount } from 'wagmi';

export default function Dashboard() {
  const { address, isConnected } = useAccount();
  const [tasks, setTasks] = useState([
    { id: 1, title: "Deploy Smart Contract", status: "Pending", priority: "High" },
    { id: 2, title: "Testnet Faucet Claim", status: "Completed", priority: "Medium" },
  ]);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-2xl font-bold mb-4">Web3 Task Dashboard</h1>
      <Card className="mb-4">
        <CardContent>
          <p>Connected Wallet: {isConnected ? address : "Not Connected"}</p>
        </CardContent>
      </Card>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Task</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Priority</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {tasks.map((task) => (
            <TableRow key={task.id}>
              <TableCell>{task.title}</TableCell>
              <TableCell>{task.status}</TableCell>
              <TableCell>{task.priority}</TableCell>
              <TableCell>
                <Button variant="secondary" size="sm">Edit</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
```
### added task creation, filtering by status, and priority handling

```
import { useState } from 'react';
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Input } from "@/components/ui/input";
import { Select, SelectItem } from "@/components/ui/select";
import { useAccount } from 'wagmi';

export default function Dashboard() {
  const { address, isConnected } = useAccount();
  const [tasks, setTasks] = useState([
    { id: 1, title: "Deploy Smart Contract", status: "Pending", priority: "High" },
    { id: 2, title: "Testnet Faucet Claim", status: "Completed", priority: "Medium" },
  ]);
  const [newTask, setNewTask] = useState("");
  const [statusFilter, setStatusFilter] = useState("");

  const addTask = () => {
    if (newTask) {
      setTasks([...tasks, { id: tasks.length + 1, title: newTask, status: "Pending", priority: "Low" }]);
      setNewTask("");
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-2xl font-bold mb-4">Web3 Task Dashboard</h1>
      <Card className="mb-4">
        <CardContent>
          <p>Connected Wallet: {isConnected ? address : "Not Connected"}</p>
        </CardContent>
      </Card>

      <div className="flex gap-2 mb-4">
        <Input value={newTask} onChange={(e) => setNewTask(e.target.value)} placeholder="New Task Title" className="text-black" />
        <Button onClick={addTask} variant="primary">Add Task</Button>
      </div>
      
      <Select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)} className="mb-4 text-black">
        <SelectItem value="">All</SelectItem>
        <SelectItem value="Pending">Pending</SelectItem>
        <SelectItem value="Completed">Completed</SelectItem>
      </Select>

      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Task</TableHead>
            <TableHead>Status</TableHead>
            <TableHead>Priority</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {tasks
            .filter(task => !statusFilter || task.status === statusFilter)
            .map((task) => (
              <TableRow key={task.id}>
                <TableCell>{task.title}</TableCell>
                <TableCell>{task.status}</TableCell>
                <TableCell>{task.priority}</TableCell>
                <TableCell>
                  <Button variant="secondary" size="sm">Edit</Button>
                </TableCell>
              </TableRow>
            ))}
        </TableBody>
      </Table>
    </div>
  );
}

```
