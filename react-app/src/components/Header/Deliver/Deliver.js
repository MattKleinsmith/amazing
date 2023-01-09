import styles from "./Deliver.module.css"

import { NavLink } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import { setShouldClearSearchBar } from "../../../store/searchbar";

export default function Deliver() {
    const dispatch = useDispatch();
    const user = useSelector(state => state.session.user);
    const address = useSelector(state => Object.values(state.addresses)[0]);

    return (
        <NavLink className={styles.wrapper} to="/addresses" style={{ textDecoration: 'none' }} onClick={() => dispatch(setShouldClearSearchBar(""))}>
            <div className={styles.icon} />
            <div className={styles.textWrapper}>
                <div className={styles.name}>{user ? `Deliver to ${user.fullname.split(" ")[0]}` : "Hello"}</div>
                <div className={styles.address}>{user && address ? `${address.city} ${address.zipcode}` : "Select your address"}</div>
            </div>
        </NavLink>
    )
}
