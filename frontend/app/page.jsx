"use client";

import { useRef } from "react";
import TaskTable from "@/components/TaskTable";
import AgentChat from "@/components/AgentChat";

export default function Home() {
  const tableRef = useRef(null);
  return (
    <main className="mx-auto max-w-[1440px]">
      <div className="mx-4 sm:mx-6">
        <AgentChat onTaskChange={() => tableRef.current.fetchTasks()} />
        <TaskTable ref={tableRef} />
      </div>
    </main>
  );
}
