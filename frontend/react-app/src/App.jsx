import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Activity, Camera, Cpu, Layout, Settings, Shield, Terminal, ArrowRight } from 'lucide-react';
import axios from 'axios';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [metrics, setMetrics] = useState({ cnn_accuracy: 0.95, rl_success_rate: 0.88, avg_reward: 14.5 });

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const res = await axios.get('http://localhost:8000/metrics');
        setMetrics(res.data);
      } catch (err) {
        console.error("Backend not reachable, using mock data");
      }
    };
    fetchMetrics();
    const interval = setInterval(fetchMetrics, 5000);
    return () => clearInterval(interval);
  }, []);

  const data = [
    { name: 'Ep 1', reward: 5 },
    { name: 'Ep 2', reward: 8 },
    { name: 'Ep 3', reward: 12 },
    { name: 'Ep 4', reward: 14 },
    { name: 'Ep 5', reward: 18 },
  ];

  return (
    <div className="flex h-screen bg-background text-slate-200">
      {/* Sidebar */}
      <div className="w-64 glass border-r border-white/10 flex flex-col p-6">
        <div className="flex items-center gap-3 mb-10">
          <div className="p-2 bg-primary rounded-lg shadow-glow">
            <Activity className="w-6 h-6 text-white" />
          </div>
          <h1 className="text-xl font-bold tracking-tight text-accent">IntelliDrive AI</h1>
        </div>

        <nav className="flex-1 space-y-2">
          {[
            { id: 'dashboard', icon: Layout, label: 'Dashboard' },
            { id: 'detection', icon: Camera, label: 'Detection' },
            { id: 'simulation', icon: Cpu, label: 'Simulation' },
            { id: 'docs', icon: Terminal, label: 'Documentation' }
          ].map(item => (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`w-full flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${activeTab === item.id ? 'bg-primary/20 text-accent neon-border shadow-glow' : 'hover:bg-white/5'
                }`}
            >
              <item.icon className="w-5 h-5" />
              <span className="font-medium">{item.label}</span>
            </button>
          ))}
        </nav>

        <div className="mt-auto glass p-4 rounded-2xl border border-white/5">
          <div className="flex items-center gap-2 text-xs text-slate-500 mb-2">
            <Shield className="w-3 h-3" />
            <span>AI CORE SECURED</span>
          </div>
          <div className="h-1 bg-white/5 rounded-full overflow-hidden">
            <motion.div
              initial={{ width: 0 }}
              animate={{ width: '80%' }}
              className="h-full bg-accent shadow-glow"
            />
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto p-10 bg-[radial-gradient(circle_at_50%_0%,#1e293b_0%,#0a0a0a_100%)]">
        <header className="flex justify-between items-center mb-12">
          <div>
            <h2 className="text-3xl font-bold mb-2 tracking-tight">System Node: <span className="text-accent">IntelliDrive-01</span></h2>
            <p className="text-slate-400 flex items-center gap-2">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
              AI Neural Engine: <span className="text-green-400 font-medium">Active & Processing</span>
            </p>
          </div>
          <div className="flex gap-4">
            <button className="glass px-4 py-2 rounded-lg border border-white/10 text-sm hover:bg-white/5 transition-all">
              Initialize Calib
            </button>
            <button className="bg-primary px-4 py-2 rounded-lg shadow-glow text-sm font-bold hover:scale-105 transition-all">
              EMERGENCY STOP
            </button>
          </div>
        </header>

        {activeTab === 'dashboard' && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8"
          >
            <StatCard label="CNN Classifier" value={`${(metrics.cnn_accuracy * 100).toFixed(1)}%`} sub="Top Accuracy" />
            <StatCard label="RL Success rate" value={`${(metrics.rl_success_rate * 100).toFixed(1)}%`} sub="Driving Efficiency" />
            <StatCard label="Reward Index" value={metrics.avg_reward.toFixed(2)} sub="+12.4% vs last session" />

            <div className="col-span-1 md:col-span-3 h-[400px] glass rounded-3xl p-8 border border-white/10 relative overflow-hidden">
              <div className="absolute top-0 right-0 p-8 opacity-5">
                <Activity className="w-64 h-64" />
              </div>
              <h3 className="text-xl font-bold mb-6 flex items-center gap-2">
                <Activity className="w-5 h-5 text-accent" />
                DQN Learning Progress
              </h3>
              <ResponsiveContainer width="100%" height="90%">
                <LineChart data={data}>
                  <CartesianGrid strokeDasharray="3 3" stroke="#222" vertical={false} />
                  <XAxis dataKey="name" stroke="#475569" axisLine={false} tickLine={false} dy={10} />
                  <YAxis stroke="#475569" axisLine={false} tickLine={false} dx={-10} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#111827', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '12px' }}
                    itemStyle={{ color: '#38BDF8' }}
                  />
                  <Line
                    type="monotone"
                    dataKey="reward"
                    stroke="#38BDF8"
                    strokeWidth={4}
                    dot={{ r: 6, fill: '#38BDF8', strokeWidth: 2, stroke: '#0a0a0a' }}
                    activeDot={{ r: 8, strokeWidth: 0 }}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </motion.div>
        )}

        {activeTab === 'detection' && (
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            className="space-y-8"
          >
            <div className="glass p-8 rounded-3xl border border-white/10">
              <div className="flex justify-between items-center mb-6">
                <div>
                  <h3 className="text-xl font-bold">Neural Vision Feed</h3>
                  <p className="text-slate-500 text-sm">YOLOv8 Real-time Tracking + Path Identification</p>
                </div>
                <div className="flex gap-2">
                  <span className="px-3 py-1 bg-green-500/10 text-green-400 text-xs rounded-full border border-green-500/20">LIVE</span>
                  <span className="px-3 py-1 bg-white/5 text-slate-400 text-xs rounded-full border border-white/10">60 FPS</span>
                </div>
              </div>
              <div className="aspect-video bg-black rounded-2xl flex items-center justify-center border border-white/10 overflow-hidden relative group">
                <img
                  src="http://localhost:8000/video-feed"
                  alt="Video Feed"
                  className="w-full h-full object-contain"
                  onError={(e) => {
                    e.target.style.display = 'none';
                    e.target.nextSibling.style.display = 'flex';
                  }}
                />
                <div style={{ display: 'none' }} className="absolute inset-0 flex items-center justify-center flex-col gap-4 bg-slate-900/50 backdrop-blur-sm">
                  <div className="w-16 h-16 border-4 border-accent border-t-transparent rounded-full animate-spin" />
                  <p className="text-slate-200 font-medium">Re-establishing Uplink...</p>
                </div>

                {/* HUD Overlays */}
                <div className="absolute top-4 left-4 p-4 border-l-2 border-accent bg-black/40 backdrop-blur-md rounded-r-lg">
                  <p className="text-[10px] text-slate-500 uppercase tracking-widest mb-1">Targeting System</p>
                  <p className="text-sm font-bold text-white">OBJECT_FOLLOW_ENABLED</p>
                </div>
              </div>

              <div className="grid grid-cols-2 gap-4 mt-6">
                <div className="p-4 bg-white/5 rounded-xl border border-white/5">
                  <p className="text-xs text-slate-500 mb-1">Detected Classes</p>
                  <p className="text-sm font-medium">Pedestrians, Vehicles, Traffic Signals</p>
                </div>
                <div className="p-4 bg-white/5 rounded-xl border border-white/5">
                  <p className="text-xs text-slate-500 mb-1">Tracking Algorithm</p>
                  <p className="text-sm font-medium text-accent">ByteTrack Neural-Assisted</p>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </div>
    </div>
  );
};

const StatCard = ({ label, value, sub }) => (
  <div className="glass p-8 rounded-3xl border border-white/10 hover:border-accent/30 hover:shadow-glow transition-all group overflow-hidden relative">
    <div className="absolute -bottom-2 -right-2 opacity-5 group-hover:opacity-10 transition-opacity">
      <ArrowRight className="w-24 h-24 -rotate-45" />
    </div>
    <p className="text-slate-500 text-xs font-bold mb-4 uppercase tracking-[0.2em]">{label}</p>
    <p className="text-5xl font-black text-white mb-2 tracking-tighter">{value}</p>
    <p className="text-sm text-slate-400 group-hover:text-accent transition-colors">{sub}</p>
  </div>
);

export default App;
