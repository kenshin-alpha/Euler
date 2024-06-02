using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.Collections;


namespace euler {
    class Problem41 {
        
        public static void Main(string[] args) {
            new Problem41().BruteForce();
            new Problem41().Digitsum();
        }

        public void BruteForce() {
            Stopwatch clock = Stopwatch.StartNew();

            int[] primes = ESieve(987654321);
            int result = 0;

            for (int i = primes.Length - 1; i >= 0; i--) {
                if(isPandigital(primes[i])){
                    result = primes[i];
                    break;
                }
            }
            
            clock.Stop();
            Console.WriteLine("The largest Pandigital prime is {0}", result);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }

        public void Digitsum() {
            Stopwatch clock = Stopwatch.StartNew();

            int[] primes = ESieve(7654321);
            int result = 0;

            for (int i = primes.Length - 1; i >= 0; i--) {
                if (isPandigital(primes[i])) {
                    result = primes[i];
                    break;
                }
            }

            clock.Stop();
            Console.WriteLine("The largest Pandigital prime is {0}", result);
            Console.WriteLine("Solution took {0} ms", clock.ElapsedMilliseconds);
        }
     
        public int[] ESieve(int upperLimit) {

            int sieveBound = (int)(upperLimit - 1) / 2;
            int upperSqrt = ((int)Math.Sqrt(upperLimit) - 1) / 2;

            BitArray PrimeBits = new BitArray(sieveBound + 1, true);

            for (int i = 1; i <= upperSqrt; i++) {
                if (PrimeBits.Get(i)) {
                    for (int j = i * 2 * (i + 1); j <= sieveBound; j += 2 * i + 1) {
                        PrimeBits.Set(j, false);
                    }
                }
            }

            List<int> numbers = new List<int>((int)(upperLimit / (Math.Log(upperLimit) - 1.08366)));
            numbers.Add(2);
            for (int i = 1; i <= sieveBound; i++) {
                if (PrimeBits.Get(i)) {
                    numbers.Add(2 * i + 1);
                }
            }

            return numbers.ToArray();
        }

        private bool isPandigital(long n) {
            int digits = 0;
            int count = 0;
            int tmp;

            while (n > 0) {
                tmp = digits;
                digits = digits | 1 << (int)((n % 10) - 1); //The minus one is there to make 1 fill the first bit and so on
                if (tmp == digits) { //Check to see if the same digit is found multiple times
                    return false;
                }

                count++;
                n /= 10;
            }

            return digits == (1 << count) - 1;
        }

    }
}
