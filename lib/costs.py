"""Phase 0: broker-accurate round-trip costs (2026-10-06).

Every figure carries its source and the date it was read. Slippage is an
ASSUMPTION (ticks per side) and is printed as one. Re-read the source before
relying on a row older than ~6 months.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Contract:
    symbol: str
    point_value: float      # $ per 1.00 index point
    tick: float             # minimum price increment, points
    commission: float       # broker $/contract/side
    exchange: float         # exchange + clearing $/contract/side
    regulatory: float       # NFA etc. $/contract/side
    source: str
    read_on: str

    @property
    def tick_value(self):
        return self.point_value * self.tick

    def round_trip(self, slip_ticks_per_side=1.0):
        fees = 2 * (self.commission + self.exchange + self.regulatory)
        return fees + 2 * slip_ticks_per_side * self.tick_value

    def round_trip_points(self, slip_ticks_per_side=1.0):
        return self.round_trip(slip_ticks_per_side) / self.point_value


IBKR = ("interactivebrokers.com/en/pricing/commissions-futures.php "
        "(IBKR Pro tiered, <=1,000 contracts/month)")
CONTRACTS = {
    # IBKR page: ES total $2.24/contract/side; MES 0.25 + 0.85 exchange + 0.01 regulatory
    "ES": Contract("ES", 50.0, 0.25, 0.85, 1.38, 0.01, IBKR, "2026-10-06"),
    "MES": Contract("MES", 5.0, 0.25, 0.25, 0.85, 0.01, IBKR, "2026-10-06"),
}

if __name__ == "__main__":
    print(f"{'sym':<5}{'fees RT $':>10}{'1 tick/side $':>15}{'2 ticks/side $':>16}{'pts @1t':>9}")
    for c in CONTRACTS.values():
        print(f"{c.symbol:<5}{c.round_trip(0):>10.2f}{c.round_trip(1):>15.2f}"
              f"{c.round_trip(2):>16.2f}{c.round_trip_points(1):>9.3f}")
    print("fees:", IBKR, "| slippage ticks are an assumption")
