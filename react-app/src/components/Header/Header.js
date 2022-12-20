import styles from './Header.module.css';

export default function Header() {
    return (
        <>
            <div className={styles.headerWrapper}>
                <div className={styles.header}>
                    "Header component"
                </div>
            </div>
            <div className={styles.line}></div>
        </>
    );
}
