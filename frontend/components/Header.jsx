import Link from "next/link"


const Header = () => {
  return (
    <header className="flex justify-between items-center py-4 px-3 sm:px-6 bg-slate-50">
        <h2 className="text-[17px] sm:text-[21px] font-semibold text-blue-500">Task Manager</h2>
        <nav className="flex space-x-3">
<Link href="/about" className="text-blue-500 text-[15px] sm:text-base">About</Link>
<Link href="/contact" className="text-blue-500 text-[15px] sm:text-base">Contact</Link>
        </nav>
    </header>
  )
}

export default Header