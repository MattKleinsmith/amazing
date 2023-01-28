import styles from "./ShippingAddress.module.css";

import AddressSelector from "./AddressSelector/AddressSelector";

export default function ShippingAddress({ showAddressSelector, setShowAddressSelector, addresses, addressIdx, setAddressIdx, onAddAddress }) {
    if (showAddressSelector)
        return <>
            <div>
                <div className={styles.step}>
                    <div className={`${styles.stepHeader} ${styles.stepNumber} ${styles.orange}`}>1</div>

                    <div className={styles.addressSelectorTitleWrapper}>
                        <div className={`${styles.stepHeader} ${styles.stepTitle} ${styles.orange} ${styles.chooseAddressTitle}`}>Choose a shipping address</div>
                        <div className={styles.simpleFlex}>
                            <div className={`${styles.changeLink}`} onClick={() => setShowAddressSelector(false)}>Close</div>
                            <div className={styles.close} onClick={() => setShowAddressSelector(false)} />
                        </div>
                    </div>
                </div>

                <div>
                    <AddressSelector addressIdx={addressIdx} setAddressIdx={setAddressIdx} addresses={addresses} />
                </div>
            </div>
        </>
    else
        return <>
            <div className={styles.step}>
                <div className={`${styles.stepHeader} ${styles.stepNumber}`}>1</div>
                <div className={`${styles.stepHeader} ${styles.stepTitle}`}>Shipping address</div>

                {addresses.length > 0 ?
                    <>
                        <div className={`${styles.stepBody}`}>
                            <div>{addresses[addressIdx].fullname}</div>
                            <div>{addresses[addressIdx].address.toUpperCase()}</div>
                            <div>{addresses[addressIdx].city.toUpperCase()}, {addresses[addressIdx].state.toUpperCase()} {addresses[addressIdx].zipcode.toUpperCase()}</div>
                        </div>
                        <div className={`${styles.changeLink}`} onClick={() => setShowAddressSelector(true)}>Change</div>
                    </>
                    :
                    <div className={`${styles.addAddress} ${styles.changeLink}`} onClick={() => onAddAddress()}>Add an address</div>
                }
            </div>
        </>
}
