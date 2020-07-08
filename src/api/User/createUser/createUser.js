export default {
  Mutation: {
    createUser: async (_, args, { prisma }) => {
      console.log(args);
      const { username, email } = args;

      // check email already registered or not.
      const exist = prisma.user.findOne({
        where: {
          email: email,
        },
      });

      if (exist) {
        throw Error("this email is already");
        return false;
      }
      try {
        const user = prisma.user.create({
          data: {
            username,
            email,
          },
        });
        return true;
      } catch {
        return false;
      }
    },
  },
};
