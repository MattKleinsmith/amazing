import styles from './Header.module.css';
import SearchBar from './SearchBar/SearchBar'
import RightHeader from './RightHeader/RightHeader'
import { useLocation } from 'react-router';
import Logo from './Logo/Logo';

export default function Header() {
    const location = useLocation();
    const excludedPaths = ["signin", "register"];
    if (excludedPaths.some(path => location.pathname.includes(path)))
        return;

    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    <Logo />
                    <SearchBar />
                    <RightHeader />
                </div>
            </div>
            <div className={styles.line}></div>
        </>
    );
}
