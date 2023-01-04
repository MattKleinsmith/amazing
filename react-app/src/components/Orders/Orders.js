import styles from "./Orders.module.css";

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";

import { getPurchases } from "../../store/purchases"

import Purchase from "./Purchase/Purchase";
import { useState } from "react";

export default function Orders() {
    const [page, setPage] = useState(1);
    const size = 10;
    const min = (page - 1) * size;
    const max = min + size;
    const purchases = useSelector(state => state.purchases).slice(min, max);

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getPurchases());
    }, [dispatch]);

    const incrementPage = () => {
        if (page * 10 < purchases.length) setPage(page + 1);
    }

    const decrementPage = () => {
        if (page > 1) setPage(page - 1);
    }

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

                <div className={styles.paginationBar}>
                    <div className={styles.paginationButton} onClick={decrementPage}>←Previous</div>
                    <div className={styles.paginationButton} onClick={incrementPage}>Next→</div>
                </div>
            </div>
        </div>
    );
}
