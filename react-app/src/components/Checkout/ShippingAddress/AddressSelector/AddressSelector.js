import React from "react";
import styles from "./AddressSelector.module.css";


export default function AddressSelector({ addressIdx, setAddressIdx, addresses }) {
    return <div className={styles.wrapper}>
        {addresses.map((address, i) => <div key={i} className={`${styles.content} ${i === addressIdx && styles.selected}`}>
            <input name="address" type="radio" id={`address_${i}`} readOnly defaultChecked={i === addressIdx} onClick={() => setAddressIdx(i)} />
            <label htmlFor={`address_${i}`} className={styles.address}>
                <span className={styles.bold}>{address.fullname} </span>
                <span>{address.address.toUpperCase()}, </span>
                <span>{address.city.toUpperCase()}, {address.state.toUpperCase()}, {address.zipcode.toUpperCase()}, {address.region.toUpperCase()}</span>
            </label>
        </div>)}
    </div>;
}
