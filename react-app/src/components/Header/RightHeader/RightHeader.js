import styles from "./RightHeader.module.css";
import AccountButton from "./AccountButton/AccountButton";
import CartButton from "./CartButton/CartButton";

export default function RightHeader() {
    return <span>
        {<div className={styles.wrapper}>
            <AccountButton />
            <CartButton />
        </div>}
    </span>
}
