import styles from "./Orders.module.css";

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";

import { getPurchases } from "../../store/purchases"

import Purchase from "./Purchase/Purchase";

export default function Orders() {
    const purchases = useSelector(state => state.purchases);

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getPurchases());
    }, [dispatch]);

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.navInfo}>Your Account {">"} <span className={styles.youAreHere}>Your Orders</span></div>
                <div className={styles.bar}>
                    <div className={styles.heading}>Your Orders</div>
                </div>
                <div className={styles.purchases}>
                    {purchases.map((purchase, i) => <Purchase key={i} purchase={purchase} />)}
                </div>
            </div>
        </div>
    );
}
