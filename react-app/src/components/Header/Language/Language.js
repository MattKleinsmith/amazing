import styles from "./Language.module.css"

export default function Language() {

    return (
        <div className={styles.wrapper}>
            <div className={`${styles.icon}`} />
            <div className={`${styles.language} noselect`}>EN</div>
        </div>
    )
}
