import styles from "./Addresses.module.css";

import { useSelector } from 'react-redux';
import { NavLink } from "react-router-dom";

import Address from "./Address/Address";

export default function Addresses() {
    const addresses = useSelector(state => Object.values(state.addresses));

    document.title = "Your Addresses"

    return (
        <div className={styles.wrapper}>
            <div className={styles.content}>
                <div className={styles.navInfo}>Your Account {">"} <span className={styles.youAreHere}>Your Addresses</span></div>
                <div className={styles.bar}>
                    <div className={styles.heading}>Your Addresses</div>
                </div>
                <div className={styles.addresses}>
                    <NavLink to="/addresses/add" className={styles.addAddress}><div className={styles.plus} /><span className={styles.addAddressText}>Add Address</span></NavLink>
                    {addresses.map((address, i) => <Address key={i} address={address} />)}
                </div>
            </div>
        </div>
    );
}
