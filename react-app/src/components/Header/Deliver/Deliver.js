import styles from "./Deliver.module.css"

import { NavLink } from "react-router-dom"
import { useSelector } from "react-redux"

export default function Deliver() {
    const user = useSelector(state => state.session.user);
    const address = useSelector(state => Object.values(state.addresses)[0]);

    return (
        <NavLink className={styles.wrapper} to="/addresses" style={{ textDecoration: 'none' }}>
            <div className={styles.icon} />
            <div className={styles.textWrapper}>
                <div className={styles.name}>{user ? `Deliver to ${user.fullname.split(" ")[0]}` : "Hello"}</div>
                <div className={styles.address}>{user && address ? `${address.city} ${address.zipcode}` : "Select your address"}</div>
            </div>
        </NavLink>
    )
}
