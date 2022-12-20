import styles from "./App.module.css";

import Header from "./components/Header/Header";
import AppRoutes from "./AppRoutes";
import Footer from "./components/Footer/Footer";

export default function App() {
  return (
    <>
      <div className={styles.pageContainer}>
        <div className={styles.contentWrapper}>
          <Header />
          <AppRoutes />
        </div>
        <Footer />
      </div>
    </>
  );
}
