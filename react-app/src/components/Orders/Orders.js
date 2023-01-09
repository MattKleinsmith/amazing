import styles from "./Orders.module.css";

import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { NavLink } from "react-router-dom";

import { getPurchases } from "../../store/purchases"
import { setShouldClearSearchBar } from "../../store/searchbar"

import Purchase from "./Purchase/Purchase";
import { useState } from "react";
import { useLocation } from "react-router";

export default function Orders() {
    const [page, setPage] = useState(1);
    const size = 10;
    const min = (page - 1) * size;
    const max = min + size;
    const allPurchases = useSelector(state => state.purchases);
    const purchases = allPurchases.slice(min, max);

    useLocation();

    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(getPurchases());
    }, [dispatch]);

    const incrementPage = () => {
        if (page * 10 < allPurchases.length) setPage(page + 1);
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
                {purchases.length === 0 &&
                    <div className={styles.emptyWrapper}>
                        <div>You have no orders.</div>
                        <NavLink to="/" className={styles.continue} onClick={() => dispatch(setShouldClearSearchBar(true))}>Continue shopping</NavLink>
                    </div>
                }

                {allPurchases.length > size && <div className={styles.paginationBar}>
                    <div className={`${styles.paginationButton} ${page <= 1 && styles.disabled} ${styles.noselect}`} onClick={decrementPage}>←Previous</div>
                    <div className={`${styles.paginationButton} ${page * 10 >= allPurchases.length && styles.disabled} ${styles.noselect}`} onClick={incrementPage}>Next→</div>
                </div>}
            </div>
        </div>
    );
}
