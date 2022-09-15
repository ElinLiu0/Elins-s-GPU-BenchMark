#Author: Elin.Liu
# Date: 2022-09-14 16:01:19
# Last Modified by:   Elin.Liu
# Last Modified time: 2022-09-14 16:01:19

# Import modules
from faker import Faker
from cudf import DataFrame
# Initialize Faker and DataFrame
faker = Faker()
df = DataFrame()
# Building DataFrame
print("Generating data...")
df['name'] = [faker.name() for _ in range(200000)]
df['address'] = [faker.address() for _ in range(200000)]
df['city'] = [faker.city() for _ in range(200000)]
df['country'] = [faker.country() for _ in range(200000)]
df['email'] = [faker.email() for _ in range(200000)]
df['phone'] = [faker.phone_number() for _ in range(200000)]
df['company'] = [faker.company() for _ in range(200000)]
df['job'] = [faker.job() for _ in range(200000)]
df['ssn'] = [faker.ssn() for _ in range(200000)]
df['credit_card'] = [faker.credit_card_number() for _ in range(200000)]
df['credit_card_provider'] = [faker.credit_card_provider()
                              for _ in range(200000)]
df['credit_card_security_code'] = [faker.credit_card_security_code()
                                   for _ in range(200000)]
df['credit_card_expire'] = [faker.credit_card_expire() for _ in range(200000)]
df['credit_card_full'] = [faker.credit_card_full() for _ in range(200000)]
df['latitude'] = [faker.latitude() for _ in range(200000)]
df['longitude'] = [faker.longitude() for _ in range(200000)]
df['date'] = [faker.date() for _ in range(200000)]
df['time'] = [faker.time() for _ in range(200000)]
df['date_time'] = [faker.date_time() for _ in range(200000)]
df['unix_time'] = [faker.unix_time() for _ in range(200000)]
df.to_csv("../../data.csv", index=False)
print("Done!")
exit(0)
