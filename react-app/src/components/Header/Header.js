import styles from './Header.module.css';
import SearchBar from './SearchBar/SearchBar'
import RightHeader from './RightHeader/RightHeader'

export default function Header() {
    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    <SearchBar />
                    <RightHeader />
                </div>
            </div>
            <div className={styles.line}></div>
        </>
    );
}
