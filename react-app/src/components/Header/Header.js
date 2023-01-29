import styles from './Header.module.css';

import { useLocation } from 'react-router';

import SearchBar from './SearchBar/SearchBar'
import RightHeader from './RightHeader/RightHeader'
import Logo from './Logo/Logo';
import LinksBar from './LinksBar/LinksBar';
import Deliver from './Deliver/Deliver';
import Language from './Language/Language';

export default function Header() {
    const location = useLocation();
    const excludedPaths = ["signin", "register", "checkout"];
    if (excludedPaths.some(path => location.pathname.includes(path)))
        return;

    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    <Logo />
                    <Deliver />
                    <SearchBar />
                    <Language />
                    <RightHeader />
                </div>
                <LinksBar />
            </div>
            <div className={styles.line} />
        </>
    );
}
