import styles from "./RightHeader.module.css";
import AccountButton from "./AccountButton/AccountButton";
import CartButton from "./CartButton/CartButton";
import ReturnsButton from "./ReturnsButton/ReturnsButton";

export default function RightHeader() {
    return <span>
        {<div className={styles.wrapper}>
            <AccountButton />
            <ReturnsButton />
            <CartButton />
        </div>}
    </span>
}
