import styles from './Header.module.css';
import SearchBar from './SearchBar/SearchBar'

export default function Header() {
    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    "Header component"
                    <SearchBar />
                </div>
            </div>
            <div className={styles.line}></div>
        </>
    );
}
