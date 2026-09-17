import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { 
  Users, 
  FileQuestion, 
  Award, 
  Clock, 
  TrendingUp,
  Building
} from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/Card';
import { Badge } from '../../components/ui/Badge';
import { Button } from '../../components/ui/Button';
import { TenantHackathonsPanel } from '../../components/admin/TenantHackathonsPanel';
import { canManageHackathons } from '../../lib/hackathons';

export const AdminDashboard: React.FC = () => {
  const { tenant, profile, role } = useAuth();
  const navigate = useNavigate();
  // Mirrors the Phase 2A RLS write policies (college_admin / super_admin).
  const canManage = canManageHackathons(role);

  return (
    <div className="space-y-6">
      {/* Dashboard Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-5">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-2xl font-bold text-slate-900">
              College Admin Console
            </h1>
            <Badge variant="default" className="capitalize">
              {profile?.role?.replace('_', ' ') || 'Admin'}
            </Badge>
          </div>
          <p className="text-xs text-slate-500 mt-1">
            Managing hackathon operations and governance for <strong className="text-slate-800">{tenant?.name || 'HackBridge'}</strong> ({tenant?.slug?.toUpperCase() || 'HackBridge'}).
          </p>
        </div>

        <div className="flex items-center gap-2">
          {canManage ? (
            <Button
              size="sm"
              className="bg-indigo-600 text-white font-semibold"
              onClick={() => navigate('/admin/hackathons/new')}
            >
              + New Hackathon
            </Button>
          ) : (
            <Badge variant="outline">Read-only role</Badge>
          )}
        </div>
      </div>

      {/* Phase 2B — REAL data read from Supabase (public.hackathons), tenant-scoped */}
      <TenantHackathonsPanel />

      {/* Everything below this marker is representative sample data, not database data.
          It is labelled on screen so it can never be mistaken for a real record. */}
      <div className="flex flex-wrap items-center gap-2 pt-2">
        <span className="text-[11px] font-semibold uppercase tracking-wider text-slate-400">
          Representative sample data (illustrative only)
        </span>
        <Badge variant="secondary">Not from the database</Badge>
      </div>

      {/* KPI Cards Grid (Matches HackBridge.pdf Spec Section 4.3) */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500">Students Registered</p>
              <p className="text-2xl font-bold text-slate-900 mt-1">324</p>
              <p className="text-[11px] text-emerald-600 font-medium mt-1 flex items-center gap-1">
                <TrendingUp className="w-3 h-3" />
                84 teams forming
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold">
              <Users className="w-5 h-5" />
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500">Problems Published</p>
              <p className="text-2xl font-bold text-slate-900 mt-1">18</p>
              <p className="text-[11px] text-amber-600 font-medium mt-1">
                4 pending committee review
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold">
              <FileQuestion className="w-5 h-5" />
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500">Active Evaluators</p>
              <p className="text-2xl font-bold text-slate-900 mt-1">24</p>
              <p className="text-[11px] text-slate-500 font-medium mt-1">
                100% CoI checked
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center font-bold">
              <Award className="w-5 h-5" />
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-5 flex items-center justify-between">
            <div>
              <p className="text-xs font-semibold text-slate-500">Tenant Plan</p>
              <p className="text-2xl font-bold text-indigo-600 mt-1 capitalize">
                {tenant?.plan || 'Enterprise'}
              </p>
              <p className="text-[11px] text-slate-500 font-medium mt-1">
                White-label active
              </p>
            </div>
            <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center font-bold">
              <Building className="w-5 h-5" />
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Active Hackathon State Machine Transition Bar */}
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <CardTitle className="text-sm flex items-center gap-2">
              <Clock className="w-4 h-4 text-indigo-600" />
              Active Event Lifecycle State: MITT Innovate 2026 (illustrative example)
            </CardTitle>
            <div className="flex items-center gap-2">
              <Badge variant="success">Registration Phase</Badge>
              <Badge variant="secondary">Sample data</Badge>
            </div>
          </div>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="grid grid-cols-2 sm:grid-cols-6 gap-2 text-center text-xs">
            <div className="p-2.5 rounded-lg bg-emerald-50 text-emerald-700 font-semibold border border-emerald-200">
              1. Draft
            </div>
            <div className="p-2.5 rounded-lg bg-emerald-50 text-emerald-700 font-semibold border border-emerald-200">
              2. Problem Intake
            </div>
            <div className="p-2.5 rounded-lg bg-indigo-600 text-white font-bold shadow-md shadow-indigo-200">
              3. Registration
            </div>
            <div className="p-2.5 rounded-lg bg-slate-100 text-slate-500 font-medium">
              4. Hacking
            </div>
            <div className="p-2.5 rounded-lg bg-slate-100 text-slate-500 font-medium">
              5. Evaluation
            </div>
            <div className="p-2.5 rounded-lg bg-slate-100 text-slate-500 font-medium">
              6. Completed
            </div>
          </div>
          <p className="text-[11px] text-slate-500">
            Current Phase: Student teams are actively forming with invite codes and selecting approved challenges.
          </p>
        </CardContent>
      </Card>

      {/* Operational Modules (Foundation Stubs) */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle className="text-sm">Problem Review Pipeline</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3 text-xs">
            <div className="p-3 border border-slate-200 rounded-lg flex items-center justify-between">
              <div>
                <p className="font-semibold text-slate-800">Edge-AI Traffic Optimization</p>
                <p className="text-slate-400 text-[11px]">Submitted by Bosch Engineering · Smart Cities</p>
              </div>
              <Badge variant="success">Approved</Badge>
            </div>
            <div className="p-3 border border-slate-200 rounded-lg flex items-center justify-between">
              <div>
                <p className="font-semibold text-slate-800">Micro-Lending Risk Modeling</p>
                <p className="text-slate-400 text-[11px]">Submitted by Razorpay · Fintech</p>
              </div>
              <Badge variant="warning">Under Review</Badge>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm">Evaluator Allocation & Judging Matrix</CardTitle>
            <Button
              size="sm"
              variant="outline"
              className="text-xs h-7 text-indigo-600 border-indigo-200 hover:bg-indigo-50"
              onClick={() => navigate('/admin/results')}
            >
              Open Matrix
            </Button>
          </CardHeader>
          <CardContent className="space-y-3 text-xs">
            <div className="p-3 border border-slate-200 rounded-lg flex items-center justify-between">
              <div>
                <p className="font-semibold text-slate-800">Double-Blind Assignment Engine</p>
                <p className="text-slate-400 text-[11px]">Auto round-robin with conflict detection</p>
              </div>
              <Badge variant="success">Phase 7 Live</Badge>
            </div>
            <div className="p-3 border border-slate-200 rounded-lg flex items-center justify-between">
              <div>
                <p className="font-semibold text-slate-800">Automated Scoring Aggregates</p>
                <p className="text-slate-400 text-[11px]">Real-time weighted averages & variance alerts</p>
              </div>
              <Badge variant="secondary">Active</Badge>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};
